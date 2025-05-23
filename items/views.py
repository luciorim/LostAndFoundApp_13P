from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Item, Comment
from .forms import ItemForm, CommentForm, RegisterForm
from django.db.models import Q


class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        queryset = Item.objects.all().order_by('-created_at')
        query = self.request.GET.get('q')
        status = self.request.GET.get('status')

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))

        if status == 'lost':
            queryset = queryset.filter(status='LOST')
        elif status == 'found':
            queryset = queryset.filter(status='FOUND')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['selected_status'] = self.request.GET.get('status', 'both')
        return context



class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'

    def post(self, request, *args, **kwargs):
        item = self.get_object()
        text = request.POST.get("text")
        if text:
            Comment.objects.create(item=item, text=text)
        return redirect('item_detail', item.id)


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')

    def form_valid(self, form):
        item = form.save(commit=False)
        item.user = self.request.user
        item.save()
        return super().form_valid(form)


class CommentCreateView(FormView):
    form_class = CommentForm

    def form_valid(self, form):
        item_id = self.kwargs['item_id']
        item = get_object_or_404(Item, id=item_id)
        comment = form.save(commit=False)
        comment.item = item
        if self.request.user.is_authenticated:
            comment.user = self.request.user
        comment.save()
        return redirect('item_detail', item.id)


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("item_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Ошибки формы:", form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_object(self):
        user_id = self.kwargs.get('user_id', None)
        if user_id:
            return get_object_or_404(User, id=user_id)
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['is_own_profile'] = self.request.user.is_authenticated and self.request.user.id == user.id
        context['user_items'] = Item.objects.filter(user=user).order_by('-created_at')
        return context


class ChangeStatusView(LoginRequiredMixin, DetailView):
    model = Item

    def post(self, request, *args, **kwargs):
        item = self.get_object()

        if request.user.is_staff or request.user == item.user:
            new_status = request.POST.get("status", "LOST").upper()
            if new_status in ["LOST", "FOUND"]:
                item.status = new_status
                item.save()

        return redirect("item_detail", item.id)

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item_list')

    def test_func(self):
        item = self.get_object()
        return self.request.user == item.user or self.request.user.is_staff
