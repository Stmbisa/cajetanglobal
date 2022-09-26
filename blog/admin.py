from django.contrib import admin

from blog.models import Blog, Feature1, Category, Author

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields= ['title', 'content']
    prepopulated_fields={"slug":"title"}
admin.site.register(Blog)

class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(Author)

class CategoryAdmin(admin.ModelAdmin):
    admin.site.register(Category)
    prepopulated_fields={"slug":"category_name"}

class Feature1Admin(admin.ModelAdmin):
    admin.site.register(Feature1)