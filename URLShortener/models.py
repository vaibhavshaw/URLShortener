from django.db import models
from .utils import generator, codeGenerator
from .validators import validate_url
from django.urls import reverse
#from django_hosts.resolvers import reverse
# Create your models here.


class ShortenDB(models.Model):
    url = models.CharField(max_length=500, validators=[validate_url, ])
    shortcode = models.CharField(max_length=10, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = codeGenerator(self)
        super(ShortenDB, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse(
            "scode", kwargs={'shortcode': self.shortcode})
        return url_path

    def get_url(self):
        url_path = reverse(
            "scode", kwargs={'shortcode': self.shortcode})
        prefix = "http://vit.ly"
        return prefix+url_path
