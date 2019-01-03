from django.contrib import admin

from .models import ProComment, ConComment, CommentOnProComment, CommentOnConComment, ReportProComment, ReportConComment


admin.site.register(ProComment)
admin.site.register(ConComment)
admin.site.register(CommentOnProComment)
admin.site.register(CommentOnConComment)
admin.site.register(ReportProComment)
admin.site.register(ReportConComment)
