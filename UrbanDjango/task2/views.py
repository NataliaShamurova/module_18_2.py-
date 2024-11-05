from django.shortcuts import render


# Create your views here.
def func_templates(request):
    return render(request, 'second_task/func_templates.html')

