from django.forms import ModelForm, Textarea 

from .models import Message, ChatRoom, Author
 
 
class PostForm(ModelForm):
 
    class Meta:
        model = Message
        fields = ['text'  ] # ,'chatRoom' 'author',,# н странице!
        widgets = {

            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class RoomForm(ModelForm):
 
    class Meta:
        model = ChatRoom
        fields = [ 'chatRoomName' ] #'chatMember', , 'chatMember' 



class ImageForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'authorAvatar' ]