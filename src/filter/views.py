from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse

import datetime 

from .models import Filter
from .forms import FilterForm
from django.shortcuts import render
from django.forms import formset_factory

def filter_create(request):
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("filter_list"))
    else:
        form = FilterForm()

    return render(request, "filter/filter_form.html", { "form": form, })


# Retrieve task list
def filter_list(request):
    tasks = Filter.objects.all()
    return render(request, "filter/filter_list.html", { "tasks": tasks})


# Retrieve a single task
def filter_detail(request, pk):
    task = get_object_or_404(Filter, pk=pk)
    return render(request, "filter/filter_detail.html", { "task": task, })


# Update a single task
def filter_update(request, pk):
    task_obj = get_object_or_404(Filter, pk=pk)
    if request.method == 'POST':
        form = FilterForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("filter_detail", args=[pk,]))
    else:
        form = FilterForm(instance=task_obj)
    return render(request, "filter/filter_form.html", { "form": form, "object": task_obj})


# Delete a single task
def filter_delete(request, pk):
    task_obj = get_object_or_404(Filter, pk=pk)
    task_obj.delete()
    return redirect(reverse("filter_list"))

def jsondata(request):
    data = list(Filter.objects.values())
    return JsonResponse(data,safe = False)

