from django import forms

from .models import (
    ProComment,
    ConComment,
    CommentOnProComment,
    CommentOnConComment,
    ReportProComment,
    ReportConComment,
)


class ProCommentForm(forms.ModelForm):
    class Meta:
        model = ProComment
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '동의하는 의견에 대한 생각 또는 이유를 알려주세요. \n추천을 많이 받을수록 상단으로 올라가요.',
                }
            )
        }

    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('댓글 내용을 입력해주세요'))
        elif len(data) > 500:
            errors.append(forms.ValidationError('댓글 내용은 500자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data


class ConCommentForm(forms.ModelForm):
    class Meta:
        model = ConComment
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '동의하는 의견에 대한 생각 또는 이유를 알려주세요. \n추천을 많이 받을수록 상단으로 올라가요.',
                }
            )
        }

    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('댓글 내용을 입력해주세요'))
        elif len(data) > 500:
            errors.append(forms.ValidationError('댓글 내용은 500자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data


class CommentOnProCommentForm(forms.ModelForm):
    class Meta:
        model = CommentOnProComment
        fields = (
            'content',
        )
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '직접 입력',
                }
            )
        }

    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('내용을 입력해주세요'))
        elif len(data) > 50:
            errors.append(forms.ValidationError('내용은 50자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data


class CommentOnConCommentForm(forms.ModelForm):
    class Meta:
        model = CommentOnConComment
        fields = (
            'content',
        )
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '의견을 입력하세요',
                }
            )
        }

    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('내용을 입력해주세요'))
        elif len(data) > 50:
            errors.append(forms.ValidationError('내용은 50자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data


class ReportProCommentForm(forms.ModelForm):
    class Meta:
        model = ReportProComment
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

    def clean_content(self):
        data = self.cleaned_data['etc_text']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('내용을 입력해주세요'))
        elif len(data) > 50:
            errors.append(forms.ValidationError('내용은 50자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data


class ReportConCommentForm(forms.ModelForm):
    class Meta:
        model = ReportConComment
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

    def clean_content(self):
        data = self.cleaned_data['etc_text']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('내용을 입력해주세요'))
        elif len(data) > 50:
            errors.append(forms.ValidationError('내용은 50자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data
