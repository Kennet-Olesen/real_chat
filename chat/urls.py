from django.urls import path
from django.views.generic import TemplateView
from chat import views


urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="index"),
    path("room/<str:slug>/", views.index, name="chat"),
    path("create/", views.room_create, name="room-create"),
    path("join/", views.room_join, name="room-join"),
    path("user_rooms/", views.user_rooms, name="user-rooms"),
]
