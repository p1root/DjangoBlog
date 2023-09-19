from django.urls import reverse_lazy
from django.views.generic import (ListView,CreateView,
                                    UpdateView,DeleteView)
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from .mixins import (FormFieldsMixin, AccessUsersMixin,
                     AccessUserMixin, FormDataSaveMixin)
from .models import User
from .forms import FormUser , SignupForm
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from .forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str   
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.core.mail import EmailMessage  
# Create your views here.


class ArticleList(AccessUsersMixin,  ListView):
    template_name = "registration/index.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(user=self.request.user)


class ArticleCreate(AccessUsersMixin, FormFieldsMixin, FormDataSaveMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"

class ArticleUpdate(AccessUsersMixin, FormFieldsMixin, AccessUserMixin, FormDataSaveMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"
    success_url = reverse_lazy("account:home")


class ArticleDelete(AccessUsersMixin, AccessUserMixin, DeleteView):
    model = Article
    template_name = "registration/article_confirm_delete.html"
    success_url = reverse_lazy("account:home")


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = FormUser
    success_url = reverse_lazy("account:home")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


class Login(LoginView):
    def get_success_url(self) -> str:
        if self.request.user.is_superuser or self.request.user.is_author():
            return reverse_lazy("account:home")
        return reverse_lazy('account:profile')


class signup(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activation link has been sent to your email id'
        message = render_to_string('registration/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('<p> ایمیل تاییدیه برای شما ارسال شد لطفا پس تایید ایمیل از طریق این <a href="{}">لینک</a> وارد شوید</p>'.format(reverse_lazy('login')))

def activate(request, uidb64, token):  
    try:  
        uid = force_str (urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('<p>ایمیل شما تایید شد از طریق این <a href="{}">لینک</a> وارد شوید</p>'.format(reverse_lazy('login')))  
    else:  
        return HttpResponse('لینک نامعتبر است')  
