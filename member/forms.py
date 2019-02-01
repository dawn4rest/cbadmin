from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import ContactChat


User = get_user_model()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['username'].label = '닉네임'
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
        self.fields['username'].label = '닉네임'
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': '(영문 대소문자/숫자/특수문자 중 2가지 이상 조합, 8자~16자)'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': '비밀번호를 다시 한 번 입력해주세요.'})
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
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': '채터박스에서 익명으로 사용 하실 닉네임을 입력해주세요.',
                }
            ),
        }


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)
    bio = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'E-mail'
        self.fields['username'].label = '닉네임'
        self.fields['bio'].label = '자기소개'
        class_update_fields = ['email', 'username', 'bio', ]
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = User
        fields = (
            'profile_image',
            'email',
            'username',
            'bio',
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
