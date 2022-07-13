# from django.shortcuts import render, redirect
# from .forms import QueryForm, StudentForm
# from .models import Student
# from django.contrib import messages
#
#
# def index(request):
#     if request.GET:
#         form = QueryForm(request.GET)
#         if form.is_valid():
#             students = form.search()
#             return render(request, 'sms_app/index.html', {
#                 'students': students,
#                 'form': form
#             })
#     else:
#         form = QueryForm()
#     return render(request, 'sms_app/index.html', context={'form': form})
#
#
# def create_student(request):
#     if request.POST:
#         form = StudentForm(request.POST)
#         print(form)
#         if form.is_valid():
#
#             form.save()
#             messages.success(request, 'Student Successfully Added')
#         else:
#             messages.error(request, 'Error saving form')
#         return redirect("index")
#     form = StudentForm()
#     return render(request, 'sms_app/create_student.html', context={'form': form})
#
#
# def detail(request, student_id):
#     student = Student.objects.get(id=student_id)
#     return render(request, 'sms_app/student_detail.html', context={'student': student})
