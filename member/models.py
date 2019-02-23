from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import models


class UserManager(BaseUserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(gender=self.model.GENDER_OTHER, *args, **kwargs)


class User(AbstractUser):
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_OTHER = 'o'
    CHOICES_GENDER = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
        (GENDER_OTHER, '기타'),
    )
    profile_image = models.ImageField(
        default='default/user.png', null=True, upload_to='user')
    bio = models.CharField(max_length=160, null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=CHOICES_GENDER, null=True, blank=True)
    like_posts = models.ManyToManyField(
        'post.Post', blank=True, related_name='like_users')
    like_comments = models.ManyToManyField(
        'comment.Comment', blank=True, related_name='like_comments')
    hate_comments = models.ManyToManyField(
        'comment.Comment', blank=True, related_name='hate_comments')

    objects = UserManager()

    def __str__(self):
        return self.username


class ContactChat(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField()

    @property
    def natural_time(self):
        return naturaltime(self.created_at)

    def __str__(self):
        return f'Chat (PK: {self.pk}, Author: {self.author.username})'
