from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ChatRoom

class ChatRoomView(APIView):
    def get(self, request):
        rooms = ChatRoom.objects.all()
        return Response({"chats": rooms})

