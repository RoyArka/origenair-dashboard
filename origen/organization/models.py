from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from colorful.fields import RGBColorField

# DEFAULT = '../origen/static/img/placeholder.jpg/'

def org_directory_path(instance, filename):
    return 'organization/logos/{0}'.format(filename)
    
class Organization(models.Model):

    name = models.CharField(max_length=25, null=False, blank=False)
    email = models.CharField(max_length=100, null=True, blank=True, default='None')
    street_name = models.CharField(max_length=100, null= True, blank=True)
    street_number = models.CharField(max_length=100, null= True, blank=True)
    city = models.CharField(max_length=100, null= True, blank=True)
    country = models.CharField(max_length=100, null= True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    description = models.TextField(max_length=255, default='', null=True, blank=True)
    color = RGBColorField(default='#1B9A4B')
    slug = models.SlugField(allow_unicode=True, unique=True)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    
    logo = models.ImageField(upload_to=org_directory_path, default='org/contemplating.png', null=True, blank=True)
   
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("organization:single", kwargs={"slug": self.slug})

    # @property
    # def get_org_avatar_url(self):
    #     if self.org_avatar and hasattr(self.org_avatar, 'url'):
    #         return self.org_avatar.url
    #     else:
    #         return "../origen/static/img/placeholder.jpg/"
    #         # self.org_avatar.url = DEFAULT
    #         # return self.org_avatar.url