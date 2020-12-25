from django.forms import ModelForm

from commentApp.models import Comment
class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
