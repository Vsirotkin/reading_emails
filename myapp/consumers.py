import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EmailConsumer(AsyncWebsocketConsumer):
    GROUP_NAME = "emails"
    MESSAGE_TYPE = "email_message"

    async def connect(self):
        """Присоединение к группе 'emails' и принятие соединения."""
        await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Отсоединение от группы 'emails' при закрытии соединения."""
        await self.channel_layer.group_discard(self.GROUP_NAME, self.channel_name)

    async def receive(self, text_data):
        """Обработка входящего сообщения и отправка его в группу 'emails'."""
        text_data_json = json.loads(text_data)
        if 'message' not in text_data_json:
            # Обработка ошибки или логирование
            return

        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.GROUP_NAME,
            {
                "type": self.MESSAGE_TYPE,
                "message": message
            }
        )

    async def email_message(self, event):
        """Отправка сообщения клиенту."""
        message = event['message']

        await self.send(text_data=json.dumps({
            "message": message
        }))
