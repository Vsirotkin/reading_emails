from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from myapp.views import EmailMessageViewSet

router = DefaultRouter()
router.register(r'email-messages', EmailMessageViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='myapp/index.html')),
    path('api/', include(router.urls)),
]