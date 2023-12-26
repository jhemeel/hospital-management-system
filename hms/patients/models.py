from django.db import models

# Create your models here.
from authy.models import User

# Create your models here.
class Patient(models.Model):
    
    class Gender(models.TextChoices):
        MALE = 'M', 'MALE'
        FEMALE = 'F', 'FEMALE'
        
        
    class Religion(models.TextChoices):
        ISLAM = 'I', 'ISLAM'
        CHRISTIANITY = 'C', 'CHRISTIANITY'
        TRADITIONAL = 'T', 'TRADITIONAL'
    
        
    slug = models.SlugField()
    avatar = models.ImageField(upload_to='doctros-images')
    prefix = models.CharField(null=True, blank=True, max_length=150) 
    last_name = models.CharField(max_length=150, null=True, blank=True)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    religion = models.CharField(null=True, blank=True, choices=Religion.choices, max_length=1)
    address = models.CharField(null=True, blank=True, max_length=300)
    
    
    def get_absolute_url(self):
        return f"admins/{self.slug}"

    
    