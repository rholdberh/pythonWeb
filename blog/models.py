from django.db import models
from webProject.settings import BASE_DIR
import os
from blog.utils.Utils import MyFileStorage


# Create your models here.
class Document(models.Model):
    mfs = MyFileStorage()
    # document = models.FileField(upload_to=os.path.join(BASE_DIR, "resources/"))
    document = models.FileField(upload_to=os.path.join(BASE_DIR, "resources/"), storage=mfs)
