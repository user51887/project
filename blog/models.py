
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()

	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)
	image = models.ImageField(upload_to='post/', default="")
	slug = models.SlugField(blank=True, null=True)

	
     
	 
	def __str__(self):
		return self.title


	def publish(self):
		self.published_date = timezone.now()
		self.save()

    #def save(self , *args , **kwargs):
	#	if not self.slug and self.name :
	#		self.slug = slugify(self.name)
	#	super(Post , self).save(*args , **kwargs)











class Comment(models.Model):
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	post = models.ForeignKey(Post , on_delete=models.CASCADE)
	votre_nom = models.CharField(max_length=50)
	content = models.TextField(null=True)
	created = models.DateTimeField(default=timezone.now)
    

	def __str__(self):
		 return str(self.content)

