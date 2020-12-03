from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()



class ArticleBase(models.Model):
    """
    this is base of posts and product
    """
    thumbnail = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    overview = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

