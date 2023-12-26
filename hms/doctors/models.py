from django.db import models
from authy.models import User

# Create your models here.
class Doctor(models.Model):
    
    class Rank(models.TextChoices):
        HOUSE_OFFICER = 'HO', 'HOUSE OFFICER'
        MEDICAL_OFFICER = 'MO', 'MEDICAL OFFICER'
        SENIOR_MDICAL_OFFICER = 'SMO', 'SENIOR MEDICAL OFFICER'
        PRINCIPAL_MEDICAL_OFFICER = 'PMO', 'PRINCIPAL MEDICAL OFFICER'
        CONSULTANT_PHYSICIAN= 'PHY', 'CONSULTANT PHYSICIAN'
        CONSULTANT_SURGEON= 'SURG', 'CONSULTANT SURGEON'
        
    class Specialty(models.TextChoices):
        CARDIOLODY = 'CARD', 'CARDIOLOGY'
        NEUROLOGY = 'NEURO', 'NEUROLOGY'
        GASTROENTEROLOGY = 'GI', 'GASTROENTEROLOGY'
        NEPHROLOGY = 'RENAL', 'NEPHROLOGY'
        PULMONOLOGIST ='RS', 'PULMONOLOGIST'
        ENDOCRINOLOGY = 'ENDO', 'ENDOCRINOLOGY'
        
        GENERAL_SURGEON = 'GS', 'GENERAL SURGEON'
        PAEDIATRIC_SURGEON = 'PS', 'PAEDIATRIC SURGEON'
        URO_SURGEON = 'URO', 'UROLOGIST'
        ORTHOPAEDIC_SURGEON = 'ORTHO', 'ORTHOPAEDIC SURGEON'
        PLASTIC_SURGEON = 'PLASTIC', 'PLASTIC SURGEON'
        NEUROSURGEON = 'NS', 'NEUROSURGEON'
        
        GYNAECOLOGY = 'O $ G', 'oBSTETRICS AND GYNAECOLOGY'
        
        ENT = 'ENT', 'ENT SURGEON'
        EYE = 'EYE', 'OPHTHALMOLOGY'
        OHTERS = 'OTHERS', 'OTHERS'
        
        
    slug = models.SlugField()
    avatar = models.ImageField(upload_to='doctros-images')
    prefix = models.CharField(null=True, blank=True, max_length=150) 
    last_name = models.CharField(max_length=150, null=True, blank=True)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.CharField(null=True, blank=True, choices=Rank.choices, max_length=4)
    specialty = models.CharField(null=True, blank=True,choices=Specialty.choices,max_length= 7)
    
    
    def get_absolute_url(self):
        return f"docotrs/{self.slug}"

    
    