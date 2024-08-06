import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EmailConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("emails", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("emails", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            "emails",
            {
                "type": "email_message",
                "message": message
            }
        )

    async def email_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            "message": message
        }))
