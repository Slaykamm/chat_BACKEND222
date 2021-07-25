
from django.urls import path
from .views import ChatRoomView

app_name = "message"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('chats/', ChatRoomView.as_view()),
]