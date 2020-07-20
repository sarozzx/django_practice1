import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    author_name=models.CharField(max_length=50,default="")
    number_of_blogs=models.CharField(default=0,max_length=5)
    def __str__(self):
        return self.author_name

class Blogs(models.Model):
    blog_name=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,default="")
    created_at=models.DateTimeField('date created')
    updated_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.blog_name

    def was_published_recently(self):
        return self.created_at>=timezone.now()-datetime.timedelta(days=1)


