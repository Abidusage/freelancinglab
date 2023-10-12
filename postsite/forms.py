from django import forms
from .models import Postsite, Comments

class PostsiteForm(forms.ModelForm):
    class Meta:
        model = Postsite
        fields = ('title', 'content')

class PostsiteUpdateForm(forms.ModelForm):
    class Meta:
        model = Postsite
        fields = ('title', 'content')

class ComentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'add a comment'}))
    class Meta:
        model = Comments
        fields = ('content',)