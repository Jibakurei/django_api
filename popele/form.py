from django import forms
from .models import BookInfo

class PostForm(forms.ModelForm):
    class mete:
        models = BookInfo
        fields = ('btitle','bpub_date'),
        pass
    pass