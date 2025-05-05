from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from items.views import (
    ItemListView, ItemDetailView, ItemCreateView, CommentCreateView,
    RegisterView, ProfileView, ChangeStatusView
)

urlpatterns = [

    #templates
    path('', ItemListView.as_view(), name='item_list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('create/', ItemCreateView.as_view(), name='item_create'),
    path('items/<int:item_id>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('change_status/<int:pk>/', ChangeStatusView.as_view(), name='change_status'),
    #rest
    path('api/', include('items.urls')),
    #silk
    path('silk/', include('silk.urls', namespace='silk')),
    #admin
    path('admin/', admin.site.urls),
]

# for loading local files
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
