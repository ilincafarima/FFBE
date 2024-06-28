from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

def validate_title_length(value):
    if len(value) < 10:
        raise ValidationError('Title must be at least 10 characters long.')

class BlogPost(models.Model):
    title = models.CharField(max_length=150, validators=[validate_title_length])
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        permissions = [
            ("can_publish", "Can publish posts"),
            ("can_edit", "Can edit posts"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', kwargs={'pk': self.pk})

    def can_edit(self, user):
        return self.author == user or user.has_perm('app_label.can_edit')

    def can_delete(self, user):
        return self.author == user or user.has_perm('app_label.can_delete')


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}: {self.body[:30]}...'

    def can_edit(self, user):
        return self.author == user or user.has_perm('app_label.can_edit_comment')

    def can_delete(self, user):
        return self.author == user or user.has_perm('app_label.can_delete_comment')


@receiver(post_save, sender=BlogPost)
def notify_author_on_new_comment(sender, instance, created, **kwargs):
    if created:
        # Placeholder for sending notification
        print(f'New post created: {instance.title} by {instance.author.username}')
