
from django.urls import path
from .views import ChatRoomView, AuthorView, MessageView, GroupView, RoomDetailView, MessageCreateView, MessageDeleteView, RoomCreateView

app_name = "message"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('chats/', ChatRoomView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('message/', MessageView.as_view()),
    path('', GroupView.as_view()),
    path('<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('<int:pk>/create/', MessageCreateView.as_view(), name='post_create'),
    path('room_create/', RoomCreateView.as_view(), name='room_create'),
    path('delete/<int:pk>', MessageDeleteView.as_view(), name='post_delete'),

    
]