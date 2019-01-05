from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Notice
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
#from formzakat.forms import EditProfileForm, ApplyZakat



@login_required(login_url="/accounts/login/")
def notice_app(request):
    if request.method == 'POST':
        note = forms.NoticeApp(request.POST, request.FILES)

        if note.is_valid():
            # save article to db
            notesave = note.save(commit=False)
            notesave.author = request.user
            notesave.save()
            return redirect('uzakat:thanks')#('formzakat:confirm')
    else:
        note = forms.NoticeApp()
    return render(request, 'notices/declare_status.html', {'note': note})