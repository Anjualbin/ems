from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView
from employer.models import MyUser
from employee.forms import SignInForm
from django.contrib.auth import authenticate,login,logout
from employer.decorators import signinrequired
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(signinrequired,name="dispatch")
class User_home(TemplateView):
    template_name = "employee/user_home.html"


class Login(TemplateView):
    template_name = "employee/index.html"
    form_class=SignInForm
    context={}
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["form"]=self.form_class()
        return context
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(username=email,password=password)
            if user:
                login(request,user)
                if request.user.is_admin:
                    return redirect("home")
                else:
                    return redirect("userhome")
            else:
                return render(request,"employee/index.html",{"form":self.form_class})
        else:
            return redirect("signin")

@method_decorator(signinrequired,name="dispatch")
class Signout(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
