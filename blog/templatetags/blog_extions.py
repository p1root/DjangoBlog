from ..models import Category, Article
from django import template
from django.db.models import Count,Q
from datetime import datetime , timedelta
register = template.Library()


@register.inclusion_tag("blog/partials/categorySidebar.html")
def categorySidebar():
    return{
        "categoris":Category.objects.publishd().annotate(count = Count('Article')).order_by('-count')[:4],
    }

@register.inclusion_tag("blog/partials/categoryNav.html")
def categoryNavbar():
    return{
        "categoris":Category.objects.publishd(),
    }
@register.inclusion_tag("blog/partials/article_mini.html")
def hotArticles():
    last_month = datetime.today() - timedelta(days=30)
    return{
        'title' : 'مقالات داغ',
        "articles":Article.objects.publishd().annotate(
            count= Count('comments' ,filter=Q(comments__posted__gt = last_month)
                )).order_by('-count' , 'publsihDate')[:5],
    }

@register.inclusion_tag("blog/partials/article_mini.html")
def lastArticles():
    last_month = datetime.today() - timedelta(days=30)
    return{
        'title' : 'آخرین مقالات',
        "articles":Article.objects.publishd().filter(publsihDate__gt = last_month),
    }