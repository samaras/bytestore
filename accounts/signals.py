from django.dispatch import reciever 
from django.db.models.signals import post_save

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, created, instance, **kwargs):
	if created:
		profile = Profile(user=instance)
		profile.save()

