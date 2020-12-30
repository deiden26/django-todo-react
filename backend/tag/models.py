from django.db import models
from .constants import TAG_COLORS

class Tag(models.Model):
  name = models.CharField(max_length=120, blank=False, null=False)
  description = models.TextField(blank=True, null=False)
  color = models.CharField(choices=TAG_COLORS, max_length=1, null=False)

  def __str__(self):
    return self.name
