from django.urls import path
from employer import views

urlpatterns=[
    path("home",views.piechart,name='home'),
    path("employee/add",views.AddEmployee.as_view(),name="addemployee"),
    path("employee/list",views.ListEmployee.as_view(),name="listemployee"),
    path("employee/edit/<int:id>",views.EditEmployee.as_view(),name="editemployee"),
    path("employee/delete/<int:id>",views.deleteEmployee,name="delemployee"),
    path("employee/viewimage/<int:id>",views.viewimage,name="image"),
    path("employee/view/<int:id>",views.ViewEmployee.as_view(),name="viewemployee"),

]