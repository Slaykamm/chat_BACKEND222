
from django.urls import path
from .views import  GroupView, RoomDetailView, MessageCreateView, MessageDeleteView, RoomCreateView, RoomUpdateView, AddUserRoomView, UserInfoView, SendDirectMessageView, RoomDeleteView

# ChatRoomView, AuthorView, MessageView, 
app_name = "message"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    # path('chats/', ChatRoomView.as_view()),
    # path('authors/', AuthorView.as_view()),
    # path('message/', MessageView.as_view()),
    path('', GroupView.as_view()),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('<int:pk>/adduser', AddUserRoomView.as_view(), name='add_user'),
    path('<int:pk>/create/', MessageCreateView.as_view(), name='post_create'),
    path('room_create/', RoomCreateView.as_view(), name='room_create'),
    path('deleteroom/<int:pk>', RoomDeleteView.as_view(), name='room_delete'),
    path('deletepost/<int:pk>', MessageDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/room_create', RoomUpdateView.as_view(), name='room_update'),
    path('userinfo/<int:pk>/', UserInfoView.as_view(), name='userinfo'),
    path('create/<int:pk>', SendDirectMessageView.as_view(), name='direct_post_create'),




    

    
]