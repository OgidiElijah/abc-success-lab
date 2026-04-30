from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=200, blank=True, help_text="e.g. Fresh Graduate, Lagos")
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question


class Service(models.Model):
    ICON_CHOICES = [
        ('bi-laptop', 'Laptop'),
        ('bi-bar-chart', 'Bar Chart'),
        ('bi-briefcase', 'Briefcase'),
        ('bi-calculator', 'Calculator'),
        ('bi-cpu', 'CPU / AI'),
        ('bi-chat-dots', 'Chat / Communication'),
        ('bi-people', 'People'),
        ('bi-graph-up', 'Graph'),
        ('bi-journal-text', 'Journal'),
        ('bi-cash-coin', 'Cash / Tax'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='bi-briefcase')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
