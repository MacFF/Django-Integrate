from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.
def chat(request):
    return TemplateResponse(request, "chat/single_chat.html")

def index(request):
    # return TemplateResponse(request, "chat/index.html")
    return render(request, "chat/index.html")

def room(request, room_name):
    print("room_name",room_name)
    print("RRRRRRRRRRRRRRRRRRRRRROOOOOOOOOMMMMMMMMMMMMMMm")

    return render(request, "chat/room.html", {"room_name": room_name})