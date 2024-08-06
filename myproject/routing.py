from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from myapp.consumers import EmailConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/email/", EmailConsumer.as_asgi()),
    ]),
})
