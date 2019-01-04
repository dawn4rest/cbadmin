from django.db import models
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import naturaltime
from multiselectfield import MultiSelectField

from post import models as post_models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta():
        abstract = True


class Comment(TimeStampedModel):
    post = models.ForeignKey(post_models.Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    type = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.author.username})'


class CommentOnComment(TimeStampedModel):
    comment = models.ForeignKey(Comment, blank=True, null=True, related_name='comment_on_comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()

    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.author.username})'


REPORT_CHOICES = (
    ('abuse', '심한 욕설을 포함하고 있어요 NO!'),
    ('infringement', '명예훼손/사생활침해 및 저작권침해!'),
    ('obscenity', '음란성 또는 청소년에게 매우 유해!'),
    ('Prosperity', '느닷없는 홍보 게시물 발견!'),
    ('irrelevant', '의견과 무관한 아무말 대잔치 댓글!'),
)
class ReportComment(TimeStampedModel):
    comment = models.ForeignKey(Comment, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    report_reason = MultiSelectField(choices=REPORT_CHOICES, blank=True, null=True)
    etc_text = models.TextField(blank=True)
