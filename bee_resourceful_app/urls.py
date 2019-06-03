from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('resources', views.ResourceView)


urlpatterns = [
    path('', include(router.urls))
]