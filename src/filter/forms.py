from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.utils.translation import gettext_lazy as _
from django.forms import modelform_factory

from .models import *
from django import forms




DAY_CHOICES = (
        ("Monday", _('Monday')),
        ("Tuesday", _("Tuesday")),
        ("Wednesday", _("Wednesday")),
        ("Thursday", _("Thursday")),
        ("Friday", _("Friday")),
        ("Saturday", _("Saturday")),
        ("Sunday", _("Sunday")),
    )  

OS_CHOICES = (
    ("Windows", "Windows"),
    ("Mac OS", "Mac OS"),
    ("Linux", "Linux"),
    ("other", "other"),
)

BYOD_CHOICES = [(0, _("Yes")),(1, _("No"))]

class FilterForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    
    
    date = forms.BooleanField(widget=forms.CheckboxInput()),
    #name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}))
    days = forms.MultipleChoiceField(choices = DAY_CHOICES,widget=forms.widgets.CheckboxSelectMultiple,label="", required=False)
    
    os = forms.MultipleChoiceField(choices = OS_CHOICES,widget=forms.widgets.CheckboxSelectMultiple(attrs={"class": "form-check"}),required=True,label="Operating System")
    
    #extra_field = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Filter
        fields = "__all__"
        labels = {
            'name':'Title',
            
        }
        widgets = {
            'name' : forms.TextInput(
                attrs={"class": "form-control"} 
            ),
            #'status' : forms.Select(attrs={'class': 'form-control'}),
            #'days':  forms.CheckboxSelectMultiple(attrs={'class': 'anyclass'}),
            'start_time' : forms.TimeInput(
                attrs={"class": "form-control",'type': 'time', 'format': '%H:%M'}
                ),
            'end_time' : forms.TimeInput(
                attrs={"class": "form-control",'type': 'time', 'format': '%H:%M'}
                ),
            'start_date' : forms.DateInput(
                attrs={"class": "form-control",'type': 'date', 'format': '%B %d'}
                ),
            'end_date' : forms.DateInput(
                attrs={"class": "form-control",'type': 'date', 'format': '%B %d'}
                ),
            'BYOD' : forms.RadioSelect(choices=BYOD_CHOICES, attrs={"class": "btn-check"})
        }
    
    def selected_days_labels(self):
        return [label for value, label in self.fields['days'].choices if value in self['days'].value()]
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """for field in self.fields: 
            print(field)
            label = {
                "placeholder": f'Rule {str(field)}',
 
            }
            self.fields[str(field)].widget.attrs.update(label)"""
        
                
class FilterExtraForm(forms.ModelForm):
    class Meta:
        model = FilterExtra
        fields = ['extra','DELETE']
        labels = {
            'extra':'',
            'DELETE': 'Supprimer'  
        }
        
        widgets = {
            'extra' : forms.TextInput(
                attrs={"class": "form-control col-3","placeholder":"Exemple: OS: Linux"} ),
            'DELETE': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }