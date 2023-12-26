from django.db import models
from authy.models import User

# Create your models here.
class Nurse(models.Model):
    
    class Rank(models.TextChoices):
        MIDWIVE = 'MW', 'MIDWIVE'
        REGISTERED_NURSE = 'RN', 'REGISTERED NURSE'
        CHEW_1 = 'JCH', 'JUNIOR CHEW'
        CHEW_2= 'CH', 'CHEW'
        
        
    slug = models.SlugField()
    avatar = models.ImageField(upload_to='doctros-images')
    prefix = models.CharField(null=True, blank=True, max_length=150) 
    last_name = models.CharField(max_length=150, null=True, blank=True)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.CharField(null=True, blank=True, choices=Rank.choices, max_length=4)
    
    
    def get_absolute_url(self):
        return f"nurses/{self.slug}"

    
    