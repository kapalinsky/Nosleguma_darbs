from django.shortcuts import render
from .forms import StudentModelForm
from .models import StudentModel, Student


def student_add(request):

    form = StudentModelForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            student_obj = Student(
                name=form.cleaned_data['name'],
                grades=form.cleaned_data['grades'],
            )
            student = StudentModel(
                name=form.cleaned_data['name'],
                grades=form.cleaned_data['grades'],
                average_grade=student_obj.get_average_grade()
            )

            student.save()

            context = {
                'student': student,
            }

            return render(
                request,
                template_name='success.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='student_add.html',
        context=context,
    )


def students_list(request):
    students_list = StudentModel.objects.all()

    return render(
        request=request,
        template_name='students_list.html',
        context={
            'students_list': students_list,
        }
    )

def get_student_info(request, student_id):
    student = StudentModel.objects.get(id=student_id)

    context = {
        'student': student,
    }

    return render(
        request=request,
        template_name='get_student.html',
        context=context,
    )
