from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Artist(models.Model):

    name = models.CharField(_("가수명"), max_length=250, default="")

    class Meta:
        verbose_name = "가수"
        verbose_name_plural = "가수"



class Song(models.Model):

    title = models.CharField(_("노래제목"), max_length=250, default="")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "노래"
        verbose_name_plural = "노래"
