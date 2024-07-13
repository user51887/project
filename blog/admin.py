from django.contrib import admin

from .models import Comment, Post 

# Register your models here.



    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
  list_display = ('title', 'author', 'published_date')
  list_filter = ('title', 'author', 'published_date')
  search_fields = ('title', 'author', 'published_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
  list_display = ('votre_nom', 'created')
  list_filter = ('votre_nom', 'created')
  search_fields = ('votre_nom', 'created')
