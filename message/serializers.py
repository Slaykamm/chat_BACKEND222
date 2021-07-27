#from chat.message.models import Message
from django.db.models import fields
from rest_framework import serializers
from .models import ChatRoom, Author, Message


# class ChatRoomSerializer(serializers.Serializer):
#     chatRoomName = serializers.CharField(max_length=200)
#     chatMember = serializers.CharField(source='chatMember.name', max_length=200)
#     message = serializers.CharField(source='message.text', max_length=200)
#     fields = [chatRoomName, chatMember, message]

class ChatRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatRoom
        fields = ['chatRoomName', 'chatMember', 'message']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name', 'authorUser', 'authorAvatar']
        
class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['author', 'text']
        

