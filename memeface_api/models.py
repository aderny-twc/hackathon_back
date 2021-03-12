from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Meme(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image', blank=True)
    user = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)


class Rating(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'meme'),)
        index_together = (('user', 'meme'),)