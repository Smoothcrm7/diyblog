from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250)
    blogger = models.ForeignKey('Profile', on_delete=models.CASCADE)
    description = models.TextField()
    post_date = models.DateField(auto_now_add=True,verbose_name="Post Date")

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def publish(self):
        self.post_date = timezone.now()
        self.save()

    def bloggerGrab(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('profile-detail', args=[str(self.blogger.id)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-post_date"]


class Comments(models.Model):
    commenter = models.CharField(max_length=50)
    post_date = models.DateTimeField(verbose_name="Post Date", auto_now_add=True)
    description = models.TextField(max_length=250, help_text='Enter comment about blog here.')
    blog_id = models.ForeignKey('Blog', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["post_date"]

    def comment(self):
        self.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.user.username)