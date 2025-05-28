from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):
    if created:
        Group.objects.get_or_create(name='Normal')
        instance.groups.add(Group.objects.get(name='Normal'))
