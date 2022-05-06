from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Employee(models.Model):

    title = models.TextField(max_length=200)
    info = models.TextField(null=True)
    # db = models.CharField(max_length=10)

    # dest = models.TextField(max_length=500)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='images/')
    # email = models.EmailField()
    # published = models.DateTimeField(default=timezone.now)



    def get_absolute_url(self):
        return reverse('employee:single', args=[self.slug])

    # class Meta:
    #     ordering = ['-published']

    def __str__(self):
        return self.title
