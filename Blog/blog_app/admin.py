from django.contrib import admin
from blog_app.models import post,Comment
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter =('status','author','created','publish') #create filters for the post
    prepopulated_fields = {'slug':('title',)} #auto create slug based on title
    search_fields=('title','body') #entered word search in title & body
    raw_id_fields = ('author',) #enter id instead of author name
    date_hierarchy='publish' #shows year on top of records, on select it will display posts of tht year
    ordering = ['status','publish'] #sort in ascending & descending

admin.site.register(post,postAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Body_comment']
    search_fields = ('Name','Body_comment')
    list_filter = ('Active',"created")

admin.site.register(Comment,CommentAdmin)
