#from chat.message.models import Message
from rest_framework import serializers
from .models import Message

# class MessagesSerializer(serializers.Serializer):

#     author = serializers.CharField(max_length=120)
#     text = serializers.CharField()


class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'text']

