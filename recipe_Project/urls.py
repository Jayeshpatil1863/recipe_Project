
from django.contrib import admin
from django.urls import path,include
from recipe_app.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('rec-',include(("recipe_app.urls","recipe_app"),namespace="recipe_app")),
    path("register-",include(("user_app.urls","user_app"),namespace="user_app")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

