from django.contrib import admin
from django.urls import path,include
from students import views

urlpatterns = [
   path('',views.student_list,name='student_list'),
   path('add/',views.add_student,name='add_student'),
   path('export-csv/',views.export_csv,name='export_csv')
]

