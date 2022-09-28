from unicodedata import category
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from .models import Blog, Feature1, Category
from .form import BlogForm, CategoryForm
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.core.mail import send_mail


def home_view(request, *args, **kwargs):
    features = Feature1.objects.all()
    blog_list = Blog.objects.all()
    categories = Category.objects.all()
    context= {
        'blog_list': blog_list,
        'features':features,
        'categories':categories,
    }
    return render (request, "blog/index.html", context) 


def warning(request):
    return render (request, "blog/warning.html") 

def about(request):
    return render (request, "blog/about.html")

class BlogList(ListView):
    model: Blog
    template_name = 'blog/allblogs.html'
    context_object_name = 'blogs'
    ordering= ['-date_posted']

    def get_queryset(self):
        return Blog.objects.all()

class BlogDetail(DetailView):
    model= Blog
    template_name = 'blog/blogdetail.html'
    context_object_name= 'blog'




class CategoryList(ListView):
    context_object_name = 'categories'
    model= Category
    template_name = 'blog/allCategorylist.html'
    ordering= ['-created_at']
    
    

def categoryView(request, pk, cats):
    category =  get_object_or_404(Category, cats= pk)
    blog_categories = Blog.objects.filter(category= cats)
    cotegory_blog_number  =len(blog_categories)
    context = {
        "category" : category,
        "blog_categories" : blog_categories,
        "cotegory_blog_number" : cotegory_blog_number,
        "cats" : cats,
    }
    return render(request, 'blog/category_blogs.html', context =context)

# Class CategoryDetailView()


class CategoryDetail(DetailView):
    model= Category
    template_name = 'blog/category_blogs.html'
    context_object_name: 'category'
    slug_field= 'category'

    # def category(self, *args, **kwargs):
    #     return category.objects.get(slug=category)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['blog_categories'] = Blog.objects.filter(category=self.get_object().pk)

        return ctx

    # def get_queryset(self):
    #     custom_id = self.kwargs['pk']
    #     return super().get_queryset().filter(blog=custom_id)

    
    

class AddCategory(CreateView):
    context_object_name = 'category'
    model= Category
    form_class = CategoryForm
    template_name = 'blog/addCategory.html'
    success_message = "Category Was added Successfully"
    success_url = reverse_lazy('blog:categories')


class UpdateCategory(UpdateView):
    model= Category
    form_class = CategoryForm
    template_name = 'blog/updateCategory.html'

class DeleteCategory(DeleteView):
    context_object_name = 'category'
    model= Category
    template_name = 'blog/deleteCategory.html'





# class BlogList(ListView):
#     model: Blog
#     template_name = 'blog/allbloglist.html'
#     context_object_name = 'blogs'
#     ordering= ['-date_posted']

#     def get_queryset(self):
#         return Blog.objects.all()


    # def test_func(self):
    #     category=self.get_object().pk      
    #     return self.get_object().manager == category

    # def get_queryset(self):
    #     a_category = Category.objects.get(category)
    #     blogs = a_category.blog_set.all()
    #     # return blogs
    #     custom_id = self.kwargs['pk']
    #     return super().get_queryset().filter(blog=custom_id)

class categoryBlogList(ListView):
    model= Blog
    template_name = 'blog/allbloglist.html'
    context_object_name = 'blogs'
    ordering= ['-date_posted']

# class BlogDetail(DetailView):
#     model= Blog
#     template_name = 'blog/blogdetail.html'
#     context_object_name= 'blog'

    # def get_success_url(self):
    #     self.object = self.get_object()
    #     category = self.object.Standard
    #     blog = self.object.blog
    #     return reverse_lazy('curriculum:lesson_detail',kwargs={'standard':category.slug,
    #                                                          'subject':blog.slug,
    #                                                          'slug':self.object.slug})

    

class AddBlog(CreateView):
    context_object_name= 'blog'
    model= Blog
    form_class = BlogForm
    template_name = 'blog/addblog.html'
    success_url = reverse_lazy('blog:category_detail')
    success_message = "Category Was added Successfully"
    pk_url_kwarg= 'blog_id'
    slug_url_kwarg='blog'
    query_pk_and_slug=True



class UpdateBlog(UpdateView):
    context_object_name= 'blog'
    model= Blog
    form_class = BlogForm
    template_name = 'blog/updateblog.html'
    success_url = reverse_lazy('blog:blog_update')


class DeleteBlog(DeleteView):
    context_object_name= 'blog'
    model= Blog
    template_name = 'blog/deleteblog.html'
    success_url = reverse_lazy('blog:category_detail')
    pk_url_kwarg='custom_id'
   
   


def search_view(request):
    query_dict= request.GET
    query = query_dict.get("q") #
    obj = None
    obj = Blog.objects.get(id = query)
    
    context = {
        'object': obj
    }
    return render (request, 'search-result.html', context=context)
    # return HttpResponseRedirect(reverse (request, 'blog:search-result', context=context))
def contact(request):
    return(request, 'contact.html')

def blog_view(request):
    context = {
        "blogs" : Blog.objects.order_by('-date_posted')[:15]
    }
    return render (request, "blog_view.html", context) 


def blog_detail_view(request, id=None):
    # blog_list = Blog.objects.all()
    blog_obj = None
    if blog_obj is not None:
        # blog_obj=Blog.objects.get(id=id)
        blog_obj=get_object_or_404(Blog, id=id)
    context= {
        'object': blog_obj, 
        # 'blog_list': blog_list
    }
    return render (request, "detail.html", context=context)
# def year_archive_view(request, year):
#     a_list = Blog.objects.filter(pub_date__year=year)
#     context ={'year':year, 'blog_list': a_list}
#     return render (request, 'blogs/year_archive.html', context)

# def month_archive_view(request, month):
#     a_list = Blog.objects.filter(pub_date__year__month=month)
#     context ={'month':month, 'blog_list': a_list}
#     return render (request, 'blogs/month_archive.html', context)


# def about(request):
#     return render (request, "about_home.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        }
        message ='''
        new message :{}

        from:{}
        
        '''.format(data['message'], data['message'] )
        send_mail(data['subject'], message, '', ['cajetanglobalvisa@gmail.com'])
        return HttpResponse('We will get in touch, thank you for contacting us ')
    return render (request, "blog/contact.html",)


