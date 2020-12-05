from django.db import models
from blog.models import ArticleBase
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model



User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title

class Comments(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    timestap = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Posts', related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.writer


class Posts(ArticleBase):
    content = RichTextField(blank=True, null=True)
    view = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    @property
    def comment_count(self):
        return Comments.objects.filter(post=self).count()

class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    value =  models.IntegerField(default=0)

    def __str__(self):
        return str(self.user) + ":" + str(self.post) + ":" + str(self.value)

    class Meta:
        unique_together = ("user", "post", "value")

