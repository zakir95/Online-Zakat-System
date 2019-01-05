from django import forms
from . import models
from bootstrap_datepicker.widgets import DatePicker
from django.forms import formset_factory
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from notices.models import Notice



class NoticeApp(forms.ModelForm):

    title = forms.CharField(label='Nama : ',
                                         widget=forms.TextInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': 'Nama Penuh',
                                             }
                                         ))

    icNo = forms.DecimalField(label='No I/C',
                              widget=forms.TextInput(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Contoh: 910121037659',
                                  }
                              ))


    class Meta:
        model = models.Notice
        fields = ['title', 'icNo']