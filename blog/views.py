from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q': q,
    })


def post_detail(requset, id):
    post = Post.objects.get(id=id)
    return render(requset, 'blog/post_detail.html', {
        'post': post,
    })