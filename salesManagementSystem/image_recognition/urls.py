from django.urls import path

from image_recognition.controllers.image_upload_controller import UserImage

from . import views

urlpatterns = [
    # path('ind', views.index, name='index'),
    path('img', UserImage.as_view(), name='index'),
]