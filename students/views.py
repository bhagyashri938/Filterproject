from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse
import csv

# Create your views here.
def add_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('student_list')
    else:
            form=StudentForm()
    return render(request,'add_student.html',{'form':form})

def student_list(request):
    students=Student.objects.all()
    #filter by name
    query_name=request.GET.get('name')
    if query_name:
        students=students.filter(name__icontains=query_name)
        
    query_name1=request.GET.get('marks')
    if query_name1:
        students=students.filter(marks=query_name1)   
        
    query_name2=request.GET.get('age')
    if query_name2:
        students=students.filter(age=query_name2)
    if 'from_date' in request.GET and 'to_date' in request.GET:
        from_date=request.GET['from_date']
        to_date=request.GET['to_date']
        students=students.filter(date_of_birth__range=[from_date,to_date])
         
        
    return render(request,'student_list.html',{'students':students})
def export_csv(request):
    a=HttpResponse(content_type='text/csv')
    a['Content-Disposition']='attachment;filename='"students.csv"
    writer=csv.writer(a)
    writer.writerow(['Name','Age','Marks','Date of Birth'])
    students=Student.objects.all()
    for student in students:
        writer.writerow([student.name,student.age,student.marks,student.date_of_birth])
    return a    
#handle date range filtering

            
            