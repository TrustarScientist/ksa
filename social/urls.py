from django.urls import path

from .views import usn
urlpatterns = [
        path('@<str:username>', usn, name="profile"),
    ]