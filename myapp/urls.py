from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import EmailMessageViewSet

router = DefaultRouter()
router.register(r'email-messages', EmailMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
