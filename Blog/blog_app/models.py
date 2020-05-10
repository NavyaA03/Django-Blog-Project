from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

class CustomManager(models.Manager): #model manager, select oly published records & define objects = CustomManager()
    def get_queryset(self):
        # return super().get_queryset().filter(status__exact="published")
        return super().get_queryset().filter(status ="published")


# Create your models here.
from taggit.managers import TaggableManager
class post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=256,unique_for_date='publish')
    author = models.ForeignKey(User,related_name = 'blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) #when post was published
    created = models.DateTimeField(auto_now_add=True) #when post was created
    updated = models.DateTimeField(auto_now = True) #when save method is called
    status =  models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects = CustomManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',) #most recent will come on top

    def __str__(self): #on submitting post title will be displayed
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args = [self.publish.year,self.publish.month,self.publish.day,self.slug])


class Comment(models.Model):
    post = models.ForeignKey(post,related_name="Comments") #post.Comments will give all comments related to posts
    Name = models.CharField(max_length=40)
    Email = models.EmailField()
    Body_comment = models.CharField(max_length=2000)

    #below fields will be updated automatically
    created = models.DateTimeField(auto_now_add=True) #when comment was created
    updated = models.DateTimeField(auto_now = True) #when save method is called
    Active = models.BooleanField(default=True) # to delete comment by admin if it's not appropriate

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "commented by {} on {}".format(self.Name,self.post)
