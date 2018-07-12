from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=10)
    created = models.DateField('Created Data ', default=timezone.now)
    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    slug = models.SlugField('Slug')
        
    def __str__(self):
        return '"%s" by %s' % (self.title, self.author)
