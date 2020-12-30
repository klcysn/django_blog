from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date"]
        
    def __str__(self):
        return self.name