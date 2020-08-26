from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
# Create your models here.



class User(AbstractUser):
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []
	objects = UserManager()
	
    
    
    
    
        
    
	


