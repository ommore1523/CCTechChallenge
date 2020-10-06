from django.db import models
from datetime import datetime

#Django model that stores images 
class Gallery(models.Model): 
    datetime = models.DateTimeField(default=datetime.now)
    photo = models.ImageField(upload_to='images/')