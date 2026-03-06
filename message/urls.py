from django.contrib import admin
from django.urls import path,include
# from message.views import MessageViewSet,UserViewSet,api_root
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from message import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"messages", views.MessageViewSet, basename = "message")
router.register(r"users", views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("register/" , views.RegisterView.as_view(), name = 'register'),
    path("login/" , views.LoginView.as_view(), name = 'login'),
]