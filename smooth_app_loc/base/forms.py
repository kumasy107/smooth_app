from django.forms import ModelForm
from . models import *

class QuestionCreateForm(ModelForm):
    class Meta:
        model=Question
        fields=['title', 'sentence']
    
    # フォームを綺麗にするための記載
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'