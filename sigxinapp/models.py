from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
# Create sigxin applications models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=200, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

@receiver(pre_save, sender=Task)
def task_handler(sender, instance, **kwargs):
    print("Pre Save Using signals")
    print(instance.title)
    instance.slug = (slugify(instance.title))
    instance.save()

#pre_save.connect(task_handler, sender=Task)


