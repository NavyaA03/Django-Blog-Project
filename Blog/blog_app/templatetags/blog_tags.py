from blog_app.models import post
from django import template
register = template.Library()

@register.simple_tag(name='Postcount')
def total_PostCount():
    return post.objects.count()


@register.inclusion_tag("blog_app/latestposts.html")
def recent_posts(count=3):
    latest_posts = post.objects.order_by('-publish')[:count]
    return {"latest_posts":latest_posts}


from django.db.models import Count

@register.assignment_tag
def mostCommented_post(count=5):
    #annotate temporarily stores no of comments to total_comments var, & to sort with no of comments use total_comments var
    return post.objects.annotate(total_comments=Count("Comments")).order_by("-total_comments")[:count]
