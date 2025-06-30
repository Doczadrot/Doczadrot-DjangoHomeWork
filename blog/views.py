from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'contents', 'preview', 'on_published', 'slug')
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'slug': self.object.slug})



class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'contents', 'preview')
    success_url = reverse_lazy('blog:blog_list')

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

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_confirm_delete.html'