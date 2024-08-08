from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from myapp.views import *

router = DefaultRouter()
router.register(r'email-messages', EmailMessageViewSet)

urlpatterns = [
    path('', email_list, name='email_list'),
    path('api/', include(router.urls)),
]
