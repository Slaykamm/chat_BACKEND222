from io import StringIO
from django.core.checks import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author, ChatRoom, Message
from .serializers import *
from .serializers import RoomApiDeleteViewSerializer

from rest_framework import viewsets
from rest_framework import permissions
import django_filters.rest_framework
from .forms import PostForm, RoomForm, ImageForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from rest_framework import serializers
from rest_framework import generics
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os




#variables for transmission between views
roomidGlobal = 0
newRoomNameGlobal = ""

class LoginViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   permission_classes = [permissions.AllowAny]
   serializer_class = UserViewSerializer

   def get_queryset(self, **kwargs):
       user = self.request.user.id
       
       print('user', user, type(user)) 
       return User.objects.filter(id=1)  #filter(username=user)



class GroupViewSet(viewsets.ModelViewSet):
   queryset = ChatRoom.objects.all()
   permission_classes = [permissions.AllowAny]
   serializer_class = GroupViewSerializer



   def get_queryset(self, **kwargs):
        chatMember = self.request.query_params.get('chatMember', None)  
        id =  self.request.query_params.get('id', None)
        chatRoomName =  self.request.query_params.get('chatRoomName', None)
        print("test otsyuda")

        if chatMember:
            return ChatRoom.objects.filter(chatMember=chatMember)

        elif chatRoomName:
            return ChatRoom.objects.filter(chatRoomName=chatRoomName)

        elif id:
            return ChatRoom.objects.filter(id=id)
            
        else:
            return ChatRoom.objects.all()



# views.py
class GroupViewUpdate(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    lookup_field = 'id'
    serializer_class = GroupViewCreateUpdateSerializer
    def update(self, request):
         print('teper tut test')
         id = self.kwargs.get('pk')
         print("ID", id)

         return id




class MessageViewSet(viewsets.ModelViewSet):
   queryset = Message.objects.all()
   permission_classes = [permissions.AllowAny]
   serializer_class = MessageViewSerializer

   def get_queryset(self, **kwargs):
        chatRoom = self.request.query_params.get('chatRoom', None)  
        author =  self.request.query_params.get('author', None)
        id =  self.request.query_params.get('id', None)
        




        if chatRoom:
            return Message.objects.filter(chatRoom=chatRoom)

        elif author:
            return Message.objects.filter(author=author)

        elif id:
            return Message.objects.filter(id=id)

        else:
            return Message.objects.all()




class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorViewSerializer
    #   filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #   fields = ['id', 'name', 'authorUser', 'authorAvatar' ]

    def save(self, *args, **kwargs):
        # Сначала модель нужно сохранить, иначе изменять/обновлять будет нечего
        super(Author, self).save(*args, **kwargs)


    def post(self, request, *args, **Kwargs):
        
        if len(request.FILES) !=0:
            file = request.FILES['imagefile']
        #   fs = FileSystemStorage() #base_url='static/imagination', location='static/imagination') 

        #  filename = fs.save(file.name, file)
            idd = self.kwargs['pk']
            newImageToBase = Author.objects.get(id = idd)
            print("000", idd, newImageToBase.name)

            newImageToBase.authorAvatar = request.FILES['imagefile']
            newImageToBase.save()


        return HttpResponse({'message':'Avatar added'}, status = 200)

 
    def get_queryset(self, **kwargs):

        name =  self.request.query_params.get('name', None)
        id =  self.request.query_params.get('id', None)
        authorAvatar = self.request.query_params.get('authorAvatar', None)



  

       # if authorUser:
       #     return Author.objects.filter(authorUser=authorUser)

        if name:
            return Author.objects.filter(name=name)

        elif id:
            return Author.objects.filter(id=id)

        else:
            return Author.objects.all()






class GroupView(ListView):
    model = ChatRoom  
    template_name = 'main.html'  
    context_object_name = 'rooms'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username 
        return context






class RoomDetailView(DetailView):
#
    template_name = 'roomdetail.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
#    queryset = Message.objects.all()
    context_object_name = 'room_detail'


 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username 
        id = self.kwargs.get('pk')
        messagesInRoom = Message.objects.filter(chatRoom_id = id)
        context['messages'] = messagesInRoom
        context['roomid'] = ChatRoom.objects.get(id = id).pk
        roomsName = ChatRoom.objects.get(id = id)
        #messagesInRoom = Message.objects.filter(chatRoom__chatRoomName = roomsName).values('text')
        usersInRoom = []
        usersList = []
        #надо перекинуть во вьюху со внутри этой
        global roomidGlobal  
        roomidGlobal = ChatRoom.objects.get(id = id).pk



        for users in Author.objects.all():

            
            if ChatRoom.objects.filter(chatRoomName = roomsName).filter(chatMember__name=users).exists():
                usersInRoom.append(users)
            else:
                usersList.append(users)

        context['usersInRoom'] = usersInRoom
        context['usersList'] = usersList

        return context

    def get_object(self, queryset=None):

        return get_object_or_404(ChatRoom, pk=self.kwargs.get('pk'))




class AddUserRoomView(DetailView):
    template_name = 'add_user.html'  
    queryset = Author.objects.all()
    context_object_name = 'room_detail'
    success_url = '/'

 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username 
        id = self.kwargs.get('pk')

        global roomidGlobal        
        roomid = roomidGlobal

        usersRoom = ChatRoom.objects.get(id = roomid)
        usersRoom.chatMember.add(Author.objects.get(id = id))
        return context




class RoomCreateView(CreateView):

    template_name = 'room_create.html'
    form_class = RoomForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username 
        return context

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.save()
        fields.chatMember.add(Author.objects.get(authorUser=self.request.user))
        return super().form_valid(form)


class RoomUpdateView(UpdateView):
    template_name = 'room_create.html'
    form_class = RoomForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username 
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return ChatRoom.objects.get(pk=id)


class RoomApiDeleteView(viewsets.ModelViewSet):
   queryset = ChatRoom.objects.all()
   permission_classes = [permissions.AllowAny]
   serializer_class = RoomApiDeleteViewSerializer
   


class RoomDeleteView(DeleteView):
    template_name = 'main.html'
    queryset = ChatRoom.objects.all()
    success_url = '/'







class MessageCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username 

        return context

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        fields = form.save(commit=False)
        fields.chatRoom = ChatRoom.objects.get(chatRoomName = ChatRoom.objects.get(id = id))
        fields.author= (Author.objects.get(authorUser=self.request.user))
        fields.save()

        return super().form_valid(form)

class MessageDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Message.objects.all()
    success_url = '/'



class UserInfoView(DetailView):

    template_name = 'userinfo.html'  
    queryset = Author.objects.all()
    context_object_name = 'userinfo'

 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username 
        id = self.kwargs.get('pk')
 
        
        user = Author.objects.get(id=id)
        context['userinfo'] = user


        return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username 

        return context





class SendDirectMessageView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    queryset = Message.objects.all()
    success_url = '/' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_user'] = self.request.user.username 
        id = self.kwargs.get('pk')
        name1 = Author.objects.get(authorUser=self.request.user)
        name2 = Author.objects.get(id = id)
        newRoomName = str(name1)+str(name2)
        global newRoomNameGlobal 
        newRoomNameGlobal = newRoomName

        if not ChatRoom.objects.filter(chatRoomName = newRoomName).exists():
            ChatRoom.objects.create(chatRoomName= newRoomName) 
            usersRoom = ChatRoom.objects.get(chatRoomName = newRoomName )
            usersRoom.chatMember.add(Author.objects.get(authorUser=self.request.user))
            usersRoom.chatMember.add(Author.objects.get(id = id))

        return context


    def form_valid(self, form):
        global newRoomNameGlobal 
        id = self.kwargs.get('pk')

        fields = form.save(commit=False)
        fields.chatRoom = ChatRoom.objects.get(chatRoomName = newRoomNameGlobal)
        fields.author = (Author.objects.get(authorUser=self.request.user))
        fields.save()

        return super().form_valid(form)

