from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.http import HttpResponseRedirect



class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date').all()[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeleteStoryView(generic.DeleteView):
    template_name = 'news/delete.html'
    model = NewsStory
    success_url = reverse_lazy('news:index')
    # Notice get_success_url is defined here and not in the model, because the model will be deleted
    # def get_success_url(self):
    #     return reverse_lazy('demos-models-dbcrud-list')

class UpdateStoryView(generic.UpdateView):
    model = NewsStory
    template_name = 'news/updateStory.html'
    fields = ['title','author', 'content', 'pub_date', 'image_url']
 
    def get_object(self, queryset=None):
        id = self.kwargs['pk']
        return self.model.objects.get(id=id)
 
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy('news:index'))