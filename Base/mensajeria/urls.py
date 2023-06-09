from django.urls import path
from .views import *

urlpatterns = [
    path('', MessageList.as_view(), name="Messages"),
    path('create', MessageCreate.as_view(), name='CreateMessage'),
    path('<pk>', MessageDetail.as_view(), name="MessageDetail"),
]