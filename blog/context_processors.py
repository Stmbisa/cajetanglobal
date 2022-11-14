from unicodedata import category
from .models import Blog, Feature1, Category

# def add_variable_to_context(request):
#     return{
#         'blog': Blog.objects.order_by('id').all(),
#         'feature1': Feature1.objects.order_by('id').all(),
#         "category":Category.objects.all()
#     }

def add_variable_to_context(request):
    categories = Category.objects.all()
    blogs= Blog.objects.order_by('id').all()
    return dict(categories=categories,blogs=blogs )