from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    CLIENT = 'client'
    WORKER = 'worker'
    FREE = 'free'
    PLUS = 'plus'
    PREMIUM = 'premium'
    ROLE_CHOICES = [
        (CLIENT, 'Client'),
        (WORKER, 'Worker'),
    ]
    MEMBERSHIP_TYPE = [
        (FREE, 'Free'),
        (PLUS, 'Plus'),
        (PREMIUM, 'Premium'),
    ]
    membership_status = models.CharField(max_length=10, choices=MEMBERSHIP_TYPE, default=FREE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CLIENT)
    worker_type = models.CharField(max_length=100, blank=True, null=True)

    # Add related_name to resolve clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',  # Rename related_name for groups
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',  # Rename related_name for user_permissions
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def clean(self):
        if self.role == self.WORKER and not self.worker_type:
            raise ValidationError("Worker type must be specified for workers")

    def save(self, *args, **kwargs):
        self.full_clean()  # Ensures clean method is called
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
