from django.contrib import admin
from .models import Author, Message, ChatRoom #, ChatRoomAuthor

# Register your models here.

admin.site.register(Author)
admin.site.register(Message)
admin.site.register(ChatRoom)

