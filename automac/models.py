from django.db import models

# Create your models here.
class GetLED(models.Model):
    device_id=models.TextField(max_length=12,primary_key=True)
    light_1 = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    light_2 = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    light_3 = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    light_4 = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)

    def __str__(self):
        return self.device_id
     

    