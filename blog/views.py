from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def about(request):
    return render(request, 'about.html')

def policy(request):
    return render(request, 'policy.html')

def contact(request):
    return render(request, 'contact.html')

def tnc(request):
    return render(request, 'tnc.html')