from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='home'),
	path('sendmail/', views.send_mail_to_all, name='send_mail'),
]
