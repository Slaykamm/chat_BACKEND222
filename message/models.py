from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30, unique=True)
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorAvatar = models.ImageField(upload_to = 'static/imagination', max_length = 100)

       
    def __str__(self):
        return self.name





class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()

       
    def __str__(self):
        return self.text



class ChatRoom(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    chatMember = models.ForeignKey(Author, on_delete=models.CASCADE)
    chatRoomName = models.CharField(max_length= 30)


       
    def __str__(self):
        return self.chatRoomName
