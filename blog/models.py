import datetime
from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import User
from django.template.defaultfilters import slugify
# from cajetanglobalvisas import settings # imported to solve ERRORS: blog.Post.author: (fields.E301) Field defines a relation with the model 'auth.User', which has been swapped out. HINT: Update the relation to point at 'settings.AUTH_USER_MODEL'.

# Create your models here.
# User = settings.AUTH_USER_MODEL #something changed 

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    role = models.CharField(max_length=100, default='editor', null=False)

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse('dashboard:profile_detail', kwargs= {'id':self.id})

class Blog(models.Model):
    image = models.ImageField(upload_to = '',default = 'no-img.jpg', blank=True)
    image1 = models.ImageField(upload_to = '',default = 'no-img.jpg', blank=True)
    image2 = models.ImageField(upload_to = '',default = 'no-img.jpg', blank=True)
    image3 = models.ImageField(upload_to = '',default = 'no-img.jpg', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='', related_name='blog_set')
    title = models.CharField(max_length=100, default='A new blog', null=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs= {'pk':self.pk} )
    
    # def get_absolute_url(self):
    #     return reverse('blog:blog_view', kwargs= {'slug':self.id} )

    def was_published_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=150)


class Category(models.Model):
    category_img = models.ImageField(upload_to = 'uploads/', blank=True, default='')
    category_name = models.CharField(max_length=100, default='1', null=False)
    description = models.TextField(max_length=350, default='This this a short description', null=False)
    created_at = models.DateField(auto_now=True, null=True, blank=True)
    slug = models.SlugField(null=False, blank=True)
    


    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs= {'slug':self.slug})

class Comment(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(default='none@email.com')
    comment_about = models.TextField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.comment_about

class Feature1(models.Model):
    image = models.ImageField(upload_to = '',default = 'images',verbose_name='blog_pic', blank=True)
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse('index_home')

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('index_home')
