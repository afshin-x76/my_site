from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()





# class PostCategory(models.Model):
#     title = models.CharField(max_length=25)

#     def __str__(self):
#         return self.title


class ArticleBase(models.Model):
    """
    this is base of posts and product
    """
    thumbnail = models.ImageField()
    title = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    overview = models.TextField()
    comment = models.IntegerField(default=5)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






# class Post(ArticleBase):
#     content = RichTextField()
#     view = models.IntegerField()
#     like = models.BooleanField(default=False)
#     category = models.ManyToManyField(PostCategory)
