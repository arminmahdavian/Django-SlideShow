from django.db import models



# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to="images/")
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True, verbose_name='Show in Menu?')
    class Meta:
        ordering = ('-published_at',)


