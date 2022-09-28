from django.urls import URLPattern, path
from . views import home_view,search_view, blog_view, blog_detail_view, search_view, \
    contact, BlogList, BlogDetail, AddBlog, UpdateBlog, DeleteBlog, CategoryList, CategoryDetail, AddCategory, \
    UpdateCategory, DeleteCategory, categoryView, warning, about

app_name = "blog"
urlpatterns = [
    path ('', home_view, name='index_home'),
    path ('search', search_view, name='search_home'),
    path ('about/', about, name='about'),
    path ('contact/', contact, name='contact'),
    path ('warning/', warning, name='warning'),
    path ('blogs/', BlogList.as_view(), name='blog_home'),
    path ('blogs/<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
    
    

    # path ('blogs', BlogList.as_view(), name='blog_home'),
    path ('blogs/categories/', CategoryList.as_view(), name='categories'),
    path ('blogs/categories/<slug:slug>/update', UpdateCategory.as_view(), name='update_category'),
    path ('blogs/categories/add', AddCategory.as_view(), name='add_category'),
    path ('blogs/categories/<slug:slug>/', BlogList.as_view(), name='category_detail'),
    path ('blogs/categories/<slug:slug>/delete/', DeleteCategory.as_view(), name='category_delete'),
    # path ('blogs/categories/<str:category>/<str:blog>/', BlogDetail.as_view(), name='blog_detail'),
    # path ('blogs/categories/<str:category>/<str:blog>/update/', UpdateBlog.as_view(), name='blog_update'),
    # path ('blogs/categories/<str:category>/<str:blog>/add/', AddBlog.as_view(), name='blog_add'),
    # path ('blogs/categories/<str:category>/<str:blog>/delete/', DeleteBlog.as_view(), name='blog_delete'),


    path ('blogs', BlogList.as_view(), name='blog_home'),
    path ('blogs/<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
    
    
    path ('contact', contact, name='contact'),
    
]