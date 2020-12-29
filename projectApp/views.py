from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse
from django.views.generic.list import MultipleObjectMixin

from articleApp.models import Article
from projectApp.forms import ProjectCreationForm
from projectApp.models import Project
from subscriptionApp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectApp/create.html'
    def get_success_url(self):
        return reverse('projectApp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectApp/detail.html'
    paginate_by = 20
    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        object_list = Article.objects.filter(project=self.get_object())
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription, **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectApp/list.html'
    paginate_by = 20
