from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import ContactChat


User = get_user_model()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        class_update_fields = ['username', 'password']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        class_update_fields = ['email', 'username', 'password1', 'password2', ]
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password1',
            'password2',
        )


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['bio'].label = '자기소개'
        self.fields['gender'].label = '성별'
        class_update_fields = ['bio', 'gender', ]
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = User
        fields = (
            'profile_image',
            'bio',
            'gender',
        )


class ContactChatForm(forms.ModelForm):
    class Meta:
        model = ContactChat
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'content',
                    'placeholder': '자유롭게 질문 또는 의견을 남겨주세요',
                }
            )
        }
