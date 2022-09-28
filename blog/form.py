from django import forms
from .models import Blog, Comment, Category, Contact


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('image','image1', 'image2','image3','category','title','content','author',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_img','category_name', 'description',]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'