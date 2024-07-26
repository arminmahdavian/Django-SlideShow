from django.db import models
from django.utils import timezone


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to="images/")
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-published_at',)
        
    def __str__(self):
        return self.title
    
    
class SlideShow(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-article__published_at',)
        
    def __str__(self):
        return self.article.title


