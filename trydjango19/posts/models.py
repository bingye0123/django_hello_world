from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

def upload_location(instance,filename):
	
	## auto generating filename after an image is uploaded, this is not the best solution though
	# filebase,extension=filename.split('.')
	# return "%s/%s.%s" %(instance.pk,instance.pk,extension)

	return "%s/%s" %(instance.pk,filename)


class Post(models.Model):

	title=models.CharField(max_length=120)
	slug=models.SlugField(unique=True)
	image=models.ImageField(null=True,blank=True,height_field='height_field',width_field='width_field',upload_to=upload_location)
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	content=models.TextField()
	last_updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts:detail',kwargs={'slug':self.slug})
		# return "%s" %(self.pk)


	class Meta:
		ordering=["-timestamp","-last_updated"]

def create_slug(instance,new_slug=None):
	slug=slugify(instance.title)
	if new_slug is not None:
		slug=new_slug
	qs=Post.objects.filter(slug=slug).order_by("-pk")
	exists=qs.exists()
	if exists:
		new_slug="%s-%s" %(slug,qs.first().pk)
		return create_slug(instance,new_slug=new_slug)
	return slug


def pre_save_post_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)

	# slug=slugify(instance.title)
	# exists=Post.objects.filter(slug=slug).exists()
	# if exists:
	# 	slug="%s-%s" %(slug,instance.pk)

	# instance.slug=slug

pre_save.connect(pre_save_post_receiver,sender=Post)









