from django import forms
from django.forms import ModelForm

from articleApp.models import Article
from projectApp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto; text-align: left'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']