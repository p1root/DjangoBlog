from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from .models import Article,Category
from django.views.generic import ListView,DetailView
from django.shortcuts import render
from django.db.models import Q
class Detail_View(DetailView):
    template_name = "blog/blog-single.html"
    def get_object(self):
        slug = self.kwargs['slug']
        article = get_object_or_404(Article.objects.publishd() , slug=slug)

        ip_address = self.request.user.ip_address
        if ip_address not in article.IPs.all():
            article.IPs.add(ip_address)
        return article

class Preview_View(DetailView):
    template_name = "blog/blog-single.html"
    def get_object(self,queryset=None):
        slug = self.kwargs['slug']
        article = get_object_or_404(Article.objects.filter(status='I') , slug=slug)
        return article

class CategoryListView(ListView):
    template_name =  "blog/category.html"
    paginate_by = 6
    def get_queryset(self):
        global cat
        slug = self.kwargs['slug']
        cat =get_object_or_404(Category.objects.publishd() , slug=slug)
        return cat.Article.publishd().order_by('-createDate')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["titleCat"] = cat
        return context
    
class HomeListView(ListView):
    template_name =  "blog/list.html"
    paginate_by = 6
    queryset= Article.objects.publishd().order_by('-createDate')
    
class SearchListView(ListView):
    template_name =  "blog/_list.html"
    paginate_by = 6
    
    def get_queryset(self):
        global text
        text = self.request.GET.get('q')
        articles = Article.objects.filter(Q(decription__icontains = text) | Q(title__icontains = text))
        
        return articles
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["titleSearch"] = text
        return context
    
def about(request):
    return render(request , "blog/about.html") 


def contact(request):
    return render(request , "blog/contact.html") 