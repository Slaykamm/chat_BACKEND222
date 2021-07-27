from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author, ChatRoom, Message
from .serializers import ChatRoomSerializer, AuthorSerializer, MessageSerializer
from .forms import PostForm, RoomForm


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ChatRoomView(APIView):
    def get(self, request, **kwargs):
        rooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(rooms, many=True)
 
        #test = ChatRoom.objects.get('message')
        #print("test", test)

        return Response({"chats": serializer.data})


class AuthorView(APIView):
    def get(self, request, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        return Response({"authors": serializer.data})

class MessageView(APIView):
    def get(self, request, **kwargs):
        authors = Message.objects.all()
        serializer = MessageSerializer(authors, many=True)

        return Response({"authors": serializer.data})



class GroupView(ListView):
    model = ChatRoom  
    template_name = 'main.html'  
    context_object_name = 'rooms'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)


    #     roomsNames = ChatRoom.objects.all()
    #     numberOfMessagesInRoomArray = []
    #     numberOfUsersInRoomArray = []
    #     for roomsName in roomsNames:

    #     #я хочу получить кол-во мессаджей в комнате
    #         messagesInRoom = Message.objects.filter(chatRoom__chatRoomName = roomsName).values('text')
    #         numberOfMessagesInRoom = len(list(messagesInRoom))
    #         numberOfMessagesInRoomArray.append(numberOfMessagesInRoom)
            
    #     # # я хочу получить кол-во юзеров
    #         usersInRoom = Message.objects.filter(chatRoom__chatRoomName = roomsName).values('author').distinct()
    #         for users in usersInRoom:
    #             userr = Author.objects.filter(id = users['author'])
    #             for user in userr:
    #             #получаем имена
    #                 numberOfUsersInRoomArray.append(user) 

    #         numberOfUsersInRoom = len(list(usersInRoom))   
       
    #     print(numberOfMessagesInRoomArray, numberOfUsersInRoomArray)

    #     context['userNumber'] = numberOfUsersInRoomArray
    #     context['messageNumber'] = numberOfMessagesInRoomArray
   
    #     return context


class RoomCreateView(CreateView):

    template_name = 'room_create.html'
    form_class = RoomForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного

        return context

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.chatMember = Author.objects.get(authorUser=self.request.user)
        print("Защибися!")
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)


        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)

class RoomDetailView(DetailView):
#
    template_name = 'roomdetail.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    queryset = Message.objects.all()
    context_object_name = 'room_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного

        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        messagesInRoom = Message.objects.filter(chatRoom_id = id)
        context['messages'] = messagesInRoom
        context['roomid'] = ChatRoom.objects.get(id = id).id

        return context



class MessageCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #context['logged_user'] = self.request.user.username  # это, чтобы в шаблоне показывать вместо логина имя залогиненного

        return context

        # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        id = self.kwargs.get('pk')

        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.author = Author.objects.get(authorUser=self.request.user)
        fields.chatRoom = ChatRoom.objects.get(chatRoomName = ChatRoom.objects.get(id = id))

        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Message.objects.all()
    success_url = '/'





