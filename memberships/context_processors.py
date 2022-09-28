from .models import Blog, Feature1, Category

def add_variable_to_context(request):
    return{
        'blog': Blog.objects.order_by('id').all(),
        'feature1': Feature1.objects.order_by('id').all(),
        "category":Category.objects.all()
    }