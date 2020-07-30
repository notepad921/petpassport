from .models import Record
from django.forms import ModelForm, TextInput, Textarea


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ["title", "record"]
        widgets = {
            "title": TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
                }),
            "record": Textarea(attrs = {
                'class': 'form-control',
                'placeholder': 'Введите описание'
                }),
            }
