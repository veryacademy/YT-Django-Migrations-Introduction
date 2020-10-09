from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name