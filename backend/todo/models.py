from django.db import models

class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  tags = models.ManyToManyField('tag.Tag', related_name='todos')

  def __str__(self):
    return self.title
