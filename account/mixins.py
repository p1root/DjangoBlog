from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from blog.models import Article

class FormFieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ["user","title" , "slug" , "decription", "publsihDate", "picture", "category", "status"]
        elif request.user.is_author:

            self.fields = ["title" , "slug" , "decription", "publsihDate", "picture", "category"]
        else:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class AccessUserMixin():
    def dispatch(self, request,pk, *args, **kwargs):
        if not request.user.is_superuser and not request.user.is_author():
            raise Http404
        article = get_object_or_404(Article ,pk=pk)
        if request.user.is_superuser or request.user == article.user:
            return super().dispatch(request, *args, **kwargs)

class AccessUsersMixin():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:    
            if request.user.is_superuser or request.user.is_author():
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('account:profile')                
        else:
            return redirect('login')

class FormDataSaveMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            article = form.save(commit=False)
            article.status = "I"
            article.user = self.request.user
            article.save()
        return super().form_valid(form)