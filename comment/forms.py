from django import forms

from .models import (
    Comment,
    CommentOnComment,
    ReportComment,
)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '동의하는 의견에 대한 생각 또는 이유를 알려주세요. \n추천을 많이 받을수록 상단으로 올라가요.',
                }
            )
        }


class CommentOnCommentForm(forms.ModelForm):
    class Meta:
        model = CommentOnComment
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '직접 입력',
                }
            )
        }


class ReportCommentForm(forms.ModelForm):
    class Meta:
        model = ReportComment
        fields = (
            'report_reason',
            'etc_text',
        )
        widgets = {
            'etc_text': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '신고 사유 직접 입력',
                }
            )
        }
