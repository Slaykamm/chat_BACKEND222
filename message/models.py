from django.db import models
from django.contrib.auth.models import User


def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.name), filename])

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30, unique=True)
#    authorUser = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    authorAvatar = models.ImageField(upload_to = 'static/imagination', max_length = 100, blank=True)#, upload_to=upload_path)

       
    def __str__(self):
        return self.name

    

#    def getUserName(self):
#        return self.authorUser


class ChatRoom(models.Model):

    chatMember = models.ManyToManyField(Author, blank=True) 
    chatRoomName = models.CharField(max_length= 30, unique=True)

    def __str__(self):
        return self.chatRoomName



class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    chatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

       

       
    def __str__(self):
        return self.text

