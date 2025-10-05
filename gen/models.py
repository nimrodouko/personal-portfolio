from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length = 10)
    myphoto = models.FileField(upload_to = 'media')

    def __str__(self):
        return self.name
#otii danger

class Projectphotos(models.Model):
    name = models.CharField(max_length= 40)
    thephoto = models.FileField(upload_to='media')
    description = models.TextField(blank = True)
    github_link = models.TextField(blank = True)

    def __str__(self):
        return self.name