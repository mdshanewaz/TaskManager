from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from TasksApp.forms import TasksForm
from TasksApp.models import TaskModel
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def addtaskView(request):
    title = 'Add Task'
    form = TasksForm

    if request.method == "POST":
        form = TasksForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save(commit=False)
            package.user = request.user
            form.save()
            print(request.FILES)
            return HttpResponseRedirect(reverse('LoginApp:profile'))

    
    context = {
        'form': form,
        'title': title,
    }

    return render(request, 'TasksApp/add_task.html', context=context)


@login_required
def tasklistView(request):
    title = 'Task List'
    user = request.user
    tasks = TaskModel.objects.filter(user=user)

    context = {
        'title': title,
        'tasks': tasks,
    }

    return render(request, 'TasksApp/task_list.html', context=context)


@login_required
def searchtasksView(request):
    title = 'Search'
    query = request.GET.get('q')
    user = request.user
    results = []
    if query:
        results = TaskModel.objects.filter(user=user, title=query)

    context = {
        'title':title,
        'query': query,
        'results': results
    }
    return render(request, 'TasksApp/search_task.html', context)


class TaskDetailView()