from django.db import models
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import naturaltime
from tagging.fields import TagField


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta():
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True , related_name='children')

    class Meta:
        unique_together = ('slug', 'parent',)   #enforcing that there can not be two
        verbose_name_plural = "categories"      #categories under a parent with same slug

    def __str__(self):                          # __str__ method elaborated later in
        full_path = [self.name]                 # post.  use __unicode__ in place of
        k = self.parent                         # __str__ if you are using python 2

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Post(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey('Category')

    title = models.CharField(max_length=160, null=True)
    thumbnail = models.ImageField(upload_to='post', blank=True, null=True)
    background = models.TextField()
    background_image1 = models.ImageField(upload_to='post', blank=True, null=True)
    background_image2 = models.ImageField(upload_to='post', blank=True, null=True)
    background_image3 = models.ImageField(upload_to='post', blank=True, null=True)
    tag = TagField()

    view_count = models.PositiveSmallIntegerField(default=0)
    share_count = models.PositiveSmallIntegerField(default=0)

    pro_title = models.CharField(max_length=160, null=True)
    con_title = models.CharField(max_length=160, null=True)

    @property
    def natural_time(self):
        return naturaltime(self.created_at)

    @property
    def likes_count(self):
        return self.like_users.all().count()

    @property
    def comment_count(self):
        all_count = self.comment_set.count()
        return all_count

    def get_cat_list(self):
        k = self.category
        breadcrumb = [""]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})'

    class Meta:
        ordering = ['-created_at']
