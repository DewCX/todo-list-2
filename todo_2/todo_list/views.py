import imp
from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {
        'todo_list': todo_list,
        'form': form
    }
    return render(request, 'todo/index.html', context)