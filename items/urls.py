from django.urls import path
from .rest_views import (
    ItemListCreateAPIView,
    ItemDetailAPIView,
    CommentCreateAPIView,
    RegisterAPIView,
    ProfileAPIView,
    ChangeStatusAPIView,
    CommentListAPIView,
    CommentDeleteAPIView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('items/', ItemListCreateAPIView.as_view(), name='api_item_list_create'),
    path('items/<int:pk>/', ItemDetailAPIView.as_view(), name='api_item_detail'),
    path('items/<int:item_id>/comment/', CommentCreateAPIView.as_view(), name='api_add_comment'),
    path('items/<int:item_id>/comments/', CommentListAPIView.as_view(), name='api_comment_list'),
    path('comments/<int:pk>/delete/', CommentDeleteAPIView.as_view(), name='api_delete_comment'),
    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('profile/', ProfileAPIView.as_view(), name='api_profile'),
    path('profile/<int:user_id>/', ProfileAPIView.as_view(), name='api_profile'),
    path('change_status/<int:pk>/', ChangeStatusAPIView.as_view(), name='api_change_status'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]