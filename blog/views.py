from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.filter(is_published=True)
    category_slug = request.GET.get('category')
    active_category = None
    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=active_category)
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'active_category': active_category,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    recent = Post.objects.filter(is_published=True).exclude(pk=post.pk)[:3]
    return render(request, 'blog/post_detail.html', {'post': post, 'recent': recent})
