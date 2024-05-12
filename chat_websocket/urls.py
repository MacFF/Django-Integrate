from django.urls import path
from chat_websocket import views

urlpatterns = [
    # path("", views.chat, name='chat'), 
    path("index/", views.index, name='index'),
    path("<str:room_name>", views.room, name="room"), 
]