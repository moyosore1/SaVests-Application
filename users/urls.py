from django.urls import path
from . import views
urlpatterns = [

	path('', views.send_mail_to_all, name='send_mail'),
]
