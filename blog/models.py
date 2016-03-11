from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish = True)



class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	# athourt = models.CharField(max_length=30)
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	objects= EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name ="Blog Entry"
		verbose_name_plural= "blog Entries"
		ordering =  ["-created"]


# class Input(models.Model):

# 	created = models.DateTimeField(auto_now_add=True)
# 	modified = models.DateTimeField(auto_now=True)
# 	body = models.TextField()
# 	publish = models.BooleanField(default=True)

# 	# objects= EntryQuerySet.as_manager()

# 	def __str__(self):
# 		return self.title


# 	class Meta:
# 		verbose_name ="modif"
# 		verbose_name_plural= "galau"
# 		ordering =  ["-created"]




class Portofolio(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	
	slug = models.SlugField(max_length=200, unique=True)
	image = models.FileField(null=True, blank=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	objects= EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name ="Portofolio Benny Danang K"
		verbose_name_plural= "Portofolio Entries"
		ordering =  ["-created"]






class Slider(models.Model):
	title = models.CharField(max_length=200)
	contain = models.TextField()
	# image = models.CharField(max_length=200)
	image = models.FileField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	objects= EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name ="Slider Benny Danang K"
		verbose_name_plural= "Slider Entries"
		ordering =  ["-created"]