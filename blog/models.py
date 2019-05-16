from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=130)
    content = models.TextField(max_length=2000)
    author = models.CharField(max_length=30)
    publish_date = models.DateTimeField()
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    


