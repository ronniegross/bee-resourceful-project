from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserList)
router.register('resources', views.ResourceView)

urlpatterns = [
    path('', include(router.urls)),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]