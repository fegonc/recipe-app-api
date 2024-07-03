"""
URL mappings for the user API.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


app_name = 'profiles_api'

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('profiles/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
