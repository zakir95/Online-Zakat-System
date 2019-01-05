from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Formzakat
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
#from formzakat.forms import EditProfileForm, ApplyZakat
#from formzakat.forms import ViewForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Formzakat, Doczakat, Confirmzakat
from django.apps import AppConfig
#from django.db.models import get_model
from django.template.loader import render_to_string
#from weasyprint import HTML
import tempfile



def formzakat_list(request):
    return render(request, 'formzakat/formzakat_list.html')


@login_required(login_url="/accounts/login/")
def apply_zakat(request):
    if request.method == 'POST':
        form = forms.ApplyZakat(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            formsave = form.save(commit=False)
            formsave.author = request.user
            formsave.save()
            return redirect('formzakat:family') #('formzakat:list')
    else:
        form = forms.ApplyZakat()
    return render(request, 'formzakat/formzakat_list.html', {'form': form})


@login_required(login_url="/accounts/login/")
def family_info(request):
    if request.method == 'POST':
        fam = forms.FamilyInfo(request.POST, request.FILES)

        if fam.is_valid():
            # save article to db
            famsave = fam.save(commit=False)
            famsave.author = request.user
            famsave.save()
            return redirect('formzakat:document')#('formzakat:family')
    else:
        fam = forms.FamilyInfo()
    return render(request, 'formzakat/family_info.html', {'fam': fam})


@login_required(login_url="/accounts/login/")
def doc_zakat(request):
    if request.method == 'POST':
        doc = forms.DocZakat(request.POST, request.FILES)

        if doc.is_valid():
            # save article to db
            docsave = doc.save(commit=False)
            docsave.author = request.user
            docsave.save()
            return redirect('formzakat:thanks') #('notices:note') #('formzakat:document')
    else:
        doc = forms.DocZakat()
    return render(request, 'formzakat/doc_list.html', {'doc': doc})


@login_required(login_url="/accounts/login/")
def thanks(request):
    return render(request,'thank_you.html')

@login_required(login_url="/accounts/login/")
def confirm_zakat(request):
    if request.method == 'POST':
        conf = forms.ConfirmZakat(request.POST, request.FILES)

        if conf.is_valid():
            # save article to db
            confsave = conf.save(commit=False)
            confsave.author = request.user
            confsave.save()
            return render(request,'thank_you.html')#('formzakat:confirm')
    else:
        conf = forms.ConfirmZakat()
    return render(request, 'formzakat/confirm_zakat.html', {'conf': conf})


#@login_required(login_url="/accounts/login/")
#def generate_pdf(request):
#    """Generate pdf."""
#    # Model data
#    sendiri = Formzakat.objects.all().order_by('last_name')

    # Rendered
#    html_string = render_to_string('bedjango/pdf.html', {'sendiri': sendiri})
#    html = HTML(string=html_string)
#    result = html.write_pdf()

    # Creating http response
 #   response = HttpResponse(content_type='application/pdf;')
 #   response['Content-Disposition'] = 'inline; filename=list_people.pdf'
 #   response['Content-Transfer-Encoding'] = 'binary'
 #   with tempfile.NamedTemporaryFile(delete=True) as output:
 #       output.write(result)
 #       output.flush()
 #       output = open(output.name, 'r')
 #       response.write(output.read())

  #  return response





