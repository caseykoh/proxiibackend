from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

# Create your models here.
class InquirySubmission(models.Model):
    class DesignType(models.TextChoices):
        CUSTOM = 'Custom'
        FLASH = 'Flash'
        FREEHAND = 'Freehand'

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=70)
    instagram = models.CharField(max_length=80)
    design_type = models.CharField(
        max_length=8,
        choices=DesignType.choices,
        default=DesignType.CUSTOM,
    )
    description = models.TextField(max_length=180)
    date = models.DateField(default=now, editable=True)

    def get_design_type(self) -> DesignType:
        # Get value from choices enum
        return self.DesignType(self.design_type)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.instagram} {self.design_type} {self.description} {self.date}"

class SubmissionImage(models.Model):
    submission = models.ForeignKey(InquirySubmission, on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return self.image_url
    

class Availability(models.Model):
    date = models.DateField()
    start_time = models.TimeField(default='12:00')
    end_time = models.TimeField(default='20:00')