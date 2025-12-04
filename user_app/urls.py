
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adduser',v.register,name="adduser"),
    path('login',v.login_user,name="login"),
    path('logout',v.logout_user,name="logout"),
    path('users/<int:id>', v.user_detail, name='users'),
    path('users/<int:id>/', v.user_detail, name='user-detail'),
    path("edit/<int:id>/",v.edit,name="edit"),
    path('edit/<int:id>', v.edit, name='edit'), 
    path('spe_list/<int:id>', v.spe_list, name='spe_list'), 

]

