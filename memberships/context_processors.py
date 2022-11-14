from .models import Blog, Category

def add_variable_to_context(request):
    blogs = Blog.objects.order_by('id').all(),
    categories =  Category.objects.all()
    return dict(blogs=blogs, categories=categories)