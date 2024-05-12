from django.urls import path, re_path
from . import consumers

websocket_urlpatterns = [
    # other websocket URLs here
    # path(r"ws/chatgpt-demo/", consumers.ChatConsumer.as_asgi(), name="chatgpt_demo"),
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]