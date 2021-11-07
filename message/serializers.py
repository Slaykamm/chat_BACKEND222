#from chat.message.models import Message
from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers
from django.http import HttpResponseRedirect
from .models import *



class UserViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'is_active', 'first_name', 'last_name', 'password' ]



class GroupViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatRoom
        fields = ['id', 'chatRoomName', 'chatMember' ]

    def create(self, validated_data):

        chatRoomName = self.validated_data.get('chatRoomName')
        chatRoomID = self.validated_data.get('id')
        print('ID', validated_data, self)

        test = ChatRoom.objects.filter(id=chatRoomID)
        print('test', test)
        if not test:
            newRoom = ChatRoom.objects.create(chatRoomName=chatRoomName) #,**validated_data)
            chatUserName = self.validated_data.get('chatMember')


     #       print("TEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEST", chatUserName)#Author.objects.get(name = chatUserName[0]))
            if chatUserName:
                for name in chatUserName:
                    newRoom.chatMember.add(Author.objects.get(name = name))
            return newRoom


class GroupViewCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'chatRoomName', 'chatMember' ]



class MessageViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'author', 'text', 'chatRoom', ]

    def create(self, validated_data):
        chatRoom = self.validated_data.get('chatRoom')  
        author =  self.validated_data.get('author')
        text =  self.validated_data.get('text')



        newMessage = Message.objects.create(author = author, chatRoom = chatRoom, text = text)
        print('test s sterilizatoah', chatRoom, author)
        return newMessage



class AuthorViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
      #  fields = ['id', 'name',  'authorAvatar' ] #'authorUser',
        fields = '__all__'





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
        model = Author
        fields = ['name', 'authorAvatar'] #, 'authorUser'
        
class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['author', 'text']
        

