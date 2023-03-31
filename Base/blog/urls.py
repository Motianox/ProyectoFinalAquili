from django.urls import path
from blog.views import *

urlpatterns = [
    path('', PostList.as_view(), name="Posts"),
    path('create', PostCreate.as_view(), name="Create"),
    path('<pk>', PostDetail.as_view(), name="Detail"),
    path('update/<pk>', PostUpdate.as_view(), name="Update"),
    path('delete/<pk>', PostDelete.as_view(), name="Delete"),
    path('aboutme', aboutme, name='AboutMe'),
]