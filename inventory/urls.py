from django.contrib import admin
from django.urls import path, include
from cash import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home/Index
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),

    # Inventory URLs
    path("inventory_list/", views.inventory_list, name="inventory_list"),
    path("inventory_create/", views.inventory_create, name="inventory_create"),
    path("inventory/<int:id>/", views.inventory_detail, name="inventory_detail"),
    path("inventory/<int:pk>/edit/", views.edit_inventory, name="edit_inventory"),
    path("inventory/<int:pk>/update/", views.inventory_update, name="inventory_update"),
    path("inventory/<int:pk>/delete/", views.inventory_delete, name="inventory_delete"),

    # Auth URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
]