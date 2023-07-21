from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.forms.models import modelformset_factory


import datetime 

from .models import Filter, FilterExtra
from .forms import FilterForm , FilterExtraForm

def index(request):
    return render(request, "filter/home.html")


def filter_create(request):
    if request.method == "POST":
        form = FilterForm(request.POST)
        ExtraFormset = modelformset_factory(FilterExtra, form=FilterExtraForm, extra=0)
        formset = ExtraFormset(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
            parent = form.save(commit=False)
            parent.save()
            for form in formset:
                child = form.save(commit=False)
                child.filter = parent
                child.save()
            print("form", form.cleaned_data)
            print("formset", formset.cleaned_data)
            return redirect(reverse("filter_list"))
    else:
        ## GET 
        #Add FilterExtra.objects.none() 
        #if we don't want display the already saved model instances
        form = FilterForm()
        ExtraFormset = modelformset_factory(FilterExtra, form=FilterExtraForm, extra=0)
        formset = ExtraFormset(queryset=FilterExtra.objects.none())

    return render(request, "filter/filter_form.html", { "form": form, "formset": formset })


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
        
        ExtraFormset = modelformset_factory(FilterExtra, form=FilterExtraForm, extra=0)
        qs = task_obj.filterextra_set.get_queryset() #[]
        formset = ExtraFormset(data=request.POST, queryset=qs)
        if all([form.is_valid(), formset.is_valid()]):
            parent = form.save(commit=False)
            
            for form in formset:
                child = form.save(commit=False)
                child.filter = parent
                if form.cleaned_data.get("DELETE"):
                    print(child.pk)
                    if child.pk: 
                        child.delete()
                else : 
                    child.save()

            parent.save()
            # Delete any forms that were marked for deletion
            #for deleted_form in formset.deleted_forms:
            #    if deleted_form.instance.pk:  # Check if the instance exists in the database
            #        deleted_form.instance.delete()
            
            print("form", form.cleaned_data)
            print("formset", formset.cleaned_data)
            return redirect(reverse("filter_detail", args=[pk,]))
    else:
        form = FilterForm(instance=task_obj)
        ExtraFormset = modelformset_factory(FilterExtra, form=FilterExtraForm, extra=0)
        qs = task_obj.filterextra_set.all()
        formset = ExtraFormset(queryset=qs)
    return render(request, "filter/filter_form.html", { "form": form, "formset":formset, "object": task_obj})


  
""" if form.prefix + '-DELETE' in request.POST:  # Check if the form is marked for deletion
        if form.instance.pk:  # Check if the instance exists in the database
            form.instance.delete()  # Delete the object from the database
            formset.deleted_forms.remove(form)
            print("here")
        else:
        child = form.save(commit=False)
        child.filter = parent
        child.save()
"""

# Delete a single task
def filter_delete(request, pk):
    task_obj = get_object_or_404(Filter, pk=pk)
    task_obj.delete()
    return redirect(reverse("filter_list"))

def jsondata(request):
    data = list(Filter.objects.values())
    return JsonResponse(data,safe = False)

