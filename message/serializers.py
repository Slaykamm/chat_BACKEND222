#from chat.message.models import Message
from django.db.models import fields
from rest_framework import serializers
from django.http import HttpResponseRedirect
from .models import *




class GroupViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatRoom
        fields = ['id', 'chatRoomName', 'chatMember' ]

    def create(self, validated_data):
        chatRoomName = validated_data.pop('chatRoomName')
        newRoom = ChatRoom.objects.create(chatRoomName=chatRoomName,**validated_data)
        return newRoom

class MessageViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'author', 'text', 'chatRoom' ]


class AuthorViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name', 'authorUser', 'authorAvatar' ]





class RoomApiDeleteViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'chatRoomName']
    
    def delete(self, validated_data):
        chatRoomName = validated_data.pop('chatRoomName')
        newRoom = ChatRoom.objects.get(chatRoomName=chatRoomName,**validated_data)
        newRoom.delete()
        return HttpResponseRedirect("/roomsAPI/")


class RoomDetailViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['name', 'authorUser', 'authorAvatar']
        
class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['author', 'text']
        

