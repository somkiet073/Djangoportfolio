from django.urls import path, include
# from .views import hello_world
from hello_world import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
