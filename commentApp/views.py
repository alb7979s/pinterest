from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleApp.models import Article
from commentApp.decorators import comment_ownership_required
from commentApp.forms import CommentCreationForm
from commentApp.models import Comment
from django.urls import reverse
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentApp/create.html'
    def get_success_url(self):
        return reverse('articleApp:detail', kwargs={'pk': self.object.article.pk})

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentApp/delete.html'
    def get_success_url(self):
        return reverse('articleApp:detail', kwargs={'pk': self.object.article.pk})