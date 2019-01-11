from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        class_update_fields = [
            'title',
            'background',
            'background_image1',
            'background_image2',
            'background_image3',
            'background_image4',
            'background_image5',
            'pro_title',
            'con_title',
            'tag',
            'category',
        ]
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update(
                {'class': 'form-control'})

    class Meta:
        model = Post
        fields = (
            'title',
            'background',
            'background_image1',
            'background_image2',
            'background_image3',
            'background_image4',
            'background_image5',
            'pro_title',
            'con_title',
            'tag',
            'category',
        )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '주제 또는 제목을 입력해주세요. (8자 이상 입력해주세요)', }),
            'background': forms.Textarea(attrs={'placeholder': '질문에 대한 더 많은 배경 정보를 알려주세요. \n상세히 적을수록 다양하고 명확한 의견을 들을 수 있어요. \n(50자 이상 입력해주세요)', }),
            'pro_title': forms.TextInput(attrs={'placeholder': '첫 번째 의견을 입력해주세요. (8자 이상 입력해주세요)', }),
            'con_title': forms.TextInput(attrs={'placeholder': '두 번째 의견을 입력해주세요. (8자 이상 입력해주세요)', }),
            'category': forms.Select(attrs={'placeholder': '카테고리를 선택해주세요.', }),
            'tag': forms.TextInput(attrs={'placeholder': '태그는 쉼표나 공백으로 분리됩니다.', }),
        }
