from django.contrib import admin

from .models import Comment, CommentOnComment, ReportComment


admin.site.register(Comment)
admin.site.register(CommentOnComment)
admin.site.register(ReportComment)
