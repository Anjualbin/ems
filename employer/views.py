from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView
from employer.models import MyUser
from employer.forms import AddEmployeeForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from employer.decorators import signinrequired
from django.utils.decorators import method_decorator

# from employer.filters import Filter

# Create your views here.
# @method_decorator(signinrequired,name="dispatch")
# class Adminhome(TemplateView):
#     template_name = "employer/basetemplate.html"

# @method_decorator(signinrequired,name="dispatch")
class AddEmployee(SuccessMessageMixin,CreateView):
    model=MyUser
    form_class = AddEmployeeForm
    template_name = "employer/add_employee.html"
    success_message = 'Employee added successfully'
    success_url = reverse_lazy("listemployee")

@method_decorator(signinrequired,name="dispatch")
class ListEmployee(ListView):
    model=MyUser
    template_name = 'employer/list_employee.html'
    context_object_name = "employees"

@method_decorator(signinrequired,name="dispatch")
class EditEmployee(UpdateView):
    model=MyUser
    form_class = AddEmployeeForm
    template_name = 'employer/edit_employee.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listemployee")

@method_decorator(signinrequired,name="dispatch")
class ViewEmployee(DetailView):
    model=MyUser
    template_name = 'employer/view_employee.html'
    pk_url_kwarg = 'id'
    context_object_name = "employee"

@signinrequired
def deleteEmployee(request,id):
    employee=MyUser.objects.get(id=id)
    employee.delete()
    return redirect("listemployee")

@signinrequired
def viewimage(request,id):
    employee=MyUser.objects.get(id=id)
    return render(request,"employer/view_image.html",{"employee":employee})

@signinrequired
def piechart(request):
    count1=MyUser.objects.filter(role="development")
    count2 = MyUser.objects.filter(role="testing")
    count3 = MyUser.objects.filter(role="hr")
    count4 = MyUser.objects.filter(role="accounting")
    data=[count1,count2,count3,count4]
    labels=["development","testing","hr","accounting"]

    return render(request,"employer/dashboard.html",{'labels':labels,"data":data})




