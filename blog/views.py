from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'contents', 'preview', 'on_published',)
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})




class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'contents', 'preview')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        form.instance.on_published = True
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = 'blog_list'

    def get_queryset(self):

        return Blog.objects.filter(on_published=True)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog_post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.count_views += 1
        obj.save()
        return obj

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
    template_name = 'blog/blog_confirm_delete.html'