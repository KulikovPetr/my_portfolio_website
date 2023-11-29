from .models import Article
from django.forms import ModelForm, TextInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'video_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое содержание'
            }),
            "full_text": Textarea(attrs={
                 'class': 'form-control',
                 'placeholder': 'Полное содержание'
            }),
            "video_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вставка для видео'
            })
        }