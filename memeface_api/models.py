from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum


class Meme(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image', blank=True)
    user = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)

    def like_rating(self):
        # ratings = Rating.objects.filter(meme=self)
        ratings = Rating.objects.filter(meme=self).aggregate(Sum('like'))['like__sum']
        print(type(ratings))
        return ratings

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(meme=self)
        for rating in ratings:
            sum += rating.like
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0


class Rating(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0, blank=False)

    class Meta:
        unique_together = (('user', 'meme'),)
        index_together = (('user', 'meme'),)
