from django.db import models

#Create blog models
#title
#pub date
#body
#image

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pubDate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    
    def pubDatePretty(self):
        return self.pubDate.strftime("%b %e %Y")