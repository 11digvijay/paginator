
from django.urls import path
from . import views

urlpatterns = [
    path('emp/',views.employeeview,name='employee'),
    path('show/',views.showemployee,name='show_emp'),
    path('update/<int:i>/',views.employeeupdate,name='update'),
    path('delete/<int:i>/',views.deleteview,name='delete'),
]