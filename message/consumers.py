import asyncio

from asgiref.sync import async_to_sync

from channels.generic.websocket import WebsocketConsumer
import json

from .models import Author, ChatRoom, Message


class ChatConsumer(WebsocketConsumer):
    # def connect(self):
    #     print("CONNN")
    #     sessions = []
    #     cha_id = self.scope["url_route"]['kwargs']
    #     chat_path = self.scope['path']
    #     self.chat_id = self.scope['path_remaining']
    #   #  print("ID Chata", cha_id)

    #     async_to_sync(self.channel_layer.group_add)("chat", self.chat_id)
    #     #async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)

    #     self.accept()


    # def disconnect(self, close_code):
    #     print("DISCCC")
    #     async_to_sync(self.channel_layer.group_discard)("chat", self.chat_id)
     

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
        
    #     message = text_data_json['message']

    #     print(text_data_json['chat_id'], text_data_json['message'], text_data_json['author_id'])

    #     Message.objects.create(author=Author.objects.get(id=text_data_json['author_id']), 
    #                            text = text_data_json['message'],  
    #                            chatRoom= ChatRoom.objects.get(id = text_data_json['chat_id']))


    #     async_to_sync(self.channel_layer.group_send)(
    #         "chat",
    #         {
    #             "type": "chat.message",
    #             "text": text_data,
    #         },
    #     )

    # def chat_message(self, event):
    #     print('!!!!!!', event)
    #     self.send(text_data=event["text"])

    # def chat_message(self, event):
    #     message = event['message']

    
    
    #     self.send(text_data=json.dumps({
    #         'event': "Send",
    #         "text": message

    #     }))




    # def chat_message(self, event):

    #     self.send(text_data=event["text"])


    def connect(self):
        async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
        self.accept()






    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("chat", self.channel_name)


    def receive(self, text_data):

        text_data_json = json.loads(text_data)
        Message.objects.create(author=Author.objects.get(id=text_data_json['author_id']), 
                               text = text_data_json['message'],  
                               chatRoom= ChatRoom.objects.get(id = text_data_json['chat_id']))

        async_to_sync(self.channel_layer.group_send)(
            "chat",
            {
                "type": "chat.message",
                "text": text_data,
            },
        )

    def chat_message(self, event):
        self.send(text_data=event["text"])