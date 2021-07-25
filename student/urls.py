

from django.urls import path
# from django.conf.urls import url
# from django.urls import urls
from .views import register_student
urlpatterns=[
    path("register/",register_student,name="register_student"),
]