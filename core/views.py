from django.shortcuts import render
from .models import Testimonial, FAQ, Service
from blog.models import Post


def home(request):
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    services = Service.objects.filter(is_active=True)[:6]
    latest_posts = Post.objects.filter(is_published=True).order_by('-published_at')[:3]
    audiences = [
        'Students',
        'Final-Year Undergraduates',
        'Fresh Graduates',
        'NYSC Members',
        'Early-Career Professionals',
        'Job Seekers',
        'Organizations Seeking Staff Training',
    ]
    return render(request, 'core/home.html', {
        'testimonials': testimonials,
        'services': services,
        'latest_posts': latest_posts,
        'audiences': audiences,
    })


def about(request):
    return render(request, 'core/about.html')


def services(request):
    all_services = Service.objects.filter(is_active=True)
    return render(request, 'core/services.html', {'services': all_services})


def contact(request):
    return render(request, 'core/contact.html')


def testimonials(request):
    all_testimonials = Testimonial.objects.filter(is_active=True)
    return render(request, 'core/testimonials.html', {'testimonials': all_testimonials})


def faqs(request):
    all_faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'core/faqs.html', {'faqs': all_faqs})