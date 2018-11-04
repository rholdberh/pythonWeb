from django.db import models
from webProject.settings import BASE_DIR
import os

# Create your models here.
class Document(models.Model):
    document = models.FileField(upload_to=os.path.join(BASE_DIR, "resources/lid.txt"))


