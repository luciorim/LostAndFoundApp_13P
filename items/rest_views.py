# items/api_views.py
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Item, Comment
from .serializers import ItemSerializer, CommentSerializer, UserSerializer, GenericCommentSerializer, \
    GenericItemSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all().prefetch_related('comments').order_by('-created_at')
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all().prefetch_related('comments')
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        item = self.get_object()
        if self.request.user.is_staff or self.request.user == item.user:
            serializer.save()
        else:
            return Response({"detail": "Not authorized to update this item."}, status=status.HTTP_403_FORBIDDEN)

    def perform_destroy(self, instance):
        if self.request.user.is_staff or self.request.user == instance.user:
            instance.delete()
        else:
            return Response({"detail": "Not authorized to delete this item."}, status=status.HTTP_403_FORBIDDEN)


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = GenericCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        item_id = self.kwargs['item_id']
        item = get_object_or_404(Item, id=item_id)
        serializer.save(item=item, user=self.request.user)


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data.get('email', ''),
                password=request.data.get('password')
            )
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        user_id = self.kwargs.get('user_id', None)
        if user_id:
            return get_object_or_404(User, id=user_id)
        if self.request.user.is_authenticated:
            return self.request.user
        return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        data = serializer.data
        data['is_own_profile'] = request.user.is_authenticated and request.user.id == user.id
        data['user_items'] = ItemSerializer(Item.objects.filter(user=user).order_by('-created_at'), many=True).data
        return Response(data)


class ChangeStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        if request.user.is_staff or request.user == item.user:
            new_status = request.data.get("status")
            if new_status in ["lost", "found", "returned"]:
                item.status = new_status
                item.save()
                return Response(ItemSerializer(item).data, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Not authorized to change status."}, status=status.HTTP_403_FORBIDDEN)

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        return Comment.objects.filter(item_id=item_id).order_by('-created_at')

class CommentDeleteAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user.is_staff or comment.user == request.user:
            return self.destroy(request, *args, **kwargs)
        return Response({"detail": "Not authorized to delete this comment."}, status=status.HTTP_403_FORBIDDEN)