from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def assign_staff_permissions(sender, instance, created, **kwargs):
    if created and instance.is_staff:
        # assign permissions to staff user
        staff_permissions = Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user'])
        staff_group, _ = Group.objects.get_or_create(name='Staff')
        staff_group.permissions.set(staff_permissions)
        instance.groups.add(staff_group)
