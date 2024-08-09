from django.test import TestCase
from channels.testing import WebsocketCommunicator
from myproject.routing import application
import asyncio

class WebSocketTests(TestCase):
    async def test_websocket_connection(self):
        communicator = WebsocketCommunicator(application, "/ws/email/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)
        await communicator.disconnect()

    async def test_websocket_send_receive(self):
        communicator = WebsocketCommunicator(application, "/ws/email/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        # Отправка сообщения
        await communicator.send_json_to({"type": "test.message", "message": "Hello, World!"})

        # Получение сообщения
        response = await communicator.receive_json_from()
        self.assertEqual(response, {"message": "Hello, World!"})

        await communicator.disconnect()

    def test_websocket_connection_sync(self):
        asyncio.run(self.test_websocket_connection())

    def test_websocket_send_receive_sync(self):
        asyncio.run(self.test_websocket_send_receive())