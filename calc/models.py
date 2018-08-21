from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age =models.IntegerField()
    pass
    
    def __unicode__(self):
        return self.name
        pass

# Create your models here.
