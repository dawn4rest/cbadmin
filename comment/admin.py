from django.contrib import admin

from .models import Comment, CommentOnComment, ReportComment, ReportCommentOnComment


admin.site.register(Comment)
admin.site.register(CommentOnComment)
admin.site.register(ReportComment)
admin.site.register(ReportCommentOnComment)
