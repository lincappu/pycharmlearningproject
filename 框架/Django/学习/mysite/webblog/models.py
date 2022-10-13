from django.db import models
from django.core.files import File


class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	address = models.CharField(max_length=200,default=None)
	phone=models.IntegerField(default=None)

	def __str__(self):
		return self.name


class Entry(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	authors = models.ManyToManyField(Author)
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	number_of_comments = models.IntegerField()
	number_of_pingbacks = models.IntegerField()
	rating = models.IntegerField()



class Dog(models.Model):
	name = models.CharField(max_length=200)
	data = models.JSONField(null=True)
	rate = models.CharField(max_length=20)

	def __str__(self):
		return self.name


# 文件对象： media_root 的位置。
class Car(models.Model):
	name=models.CharField(max_length=20)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	phote=models.ImageField(upload_to='cars/')




