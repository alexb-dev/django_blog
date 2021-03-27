from django.contrib import admin

# a new import
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    """
    Inline model to be attachd to posts form.

    Note, because of  many-to-many it has 'through'
    """
    model = Category.posts.through


class PostAdmin (admin.ModelAdmin):
    """
    Custom ModelAdmin  form for Post with inlined categories
    """
    inlines = [CategoryInline,]

class CategoryAdmin(admin.ModelAdmin):
    """
    Custom ModelAdmin for Categories form w/ hidden posts field
    """
    fields = ('name', 'description')

# and a new admin registration
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
