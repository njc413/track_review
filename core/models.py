from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Review(models.Model):
    Track = models.CharField(max_length=300)
    Review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__ (self):
        return self.Track

    def get_absolute_url(self):
        return reverse("review_detail", args=[self.id])