from django import forms
from . import models
from bootstrap_datepicker.widgets import DatePicker
from django.forms import formset_factory
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from formzakat.models import Formzakat, Doczakat, Familyinfo



class ApplyZakat(forms.ModelForm):

    title = forms.CharField(label='Nama Penuh',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Nama Penuh Anda.....',
                                }
                            ))

    icNo = forms.DecimalField(label='No I/C',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Contoh: 910121037659',
                                }
                            ))

    body = forms.CharField(label='Alamat',
                           widget=forms.Textarea(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    poskod = forms.DecimalField(label='Poskod',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    bandar = forms.CharField(label='Bandar',
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '',
                                    }
                                ))

    noTel = forms.DecimalField(label='No Telefon',
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Contoh: 0125932519',
                                    }
                                ))

    DOB = forms.CharField(label='Tarikh Lahir',
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Contoh: 21 Oktober 1991',
                                    }
                                ))

    tLahir = forms.CharField(label='Tempat Lahir',
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '',
                                    }
                                ))

#    statusDiri = forms.CharField(label='Status Perkahwinan',
#                                widget=forms.Select(
#                                    attrs={
#                                        'class': 'form-control',
#                                        'placeholder': '',
#                                    }
#                                ))

#    Kesihatan = forms.CharField(label='Status Kesihatan',
#                                widget=forms.RadioSelect(
#                                    attrs={
#                                        'class': 'form-control',
#                                        'placeholder': '',
#                                    }
#                                ))

    ProgramPengajian = forms.CharField(label='Program Pengajian',
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '',
                                    }
                                ))

#    Fakulti = forms.CharField(label='Fakulti',
#                                       widget=forms.TextInput(
#                                           attrs={
#                                               'class': 'form-control',
#                                               'placeholder': '',
#                                           }
#                                       ))

#    PeringkatPengajian = forms.CharField(label='Peringkat Pengajian',
#                                       widget=forms.TextInput(
#                                           attrs={
#                                               'class': 'form-control',
#                                               'placeholder': '',
#                                           }
#                                       ))

    TempohPengajian = forms.CharField(label='Tempoh Pengajian',
                                         widget=forms.TextInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': '',
                                             }
                                         ))

    CPGA = forms.DecimalField(label='CGPA',
                                         widget=forms.TextInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': '',
                                             }
                                         ))

    Penaja = forms.CharField(label='Penaja',
                                         widget=forms.TextInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': 'Contoh: PTPTN',
                                             }
                                         ))
#    StatusPenaja = forms.CharField(label='Status Penajaan',
#                                         widget=forms.RadioSelect(
#                                             attrs={
#                                                 'class': 'form-control',
#                                                 'placeholder': '',
#                                             }
#                                         ))

    JumlahTajaan = forms.DecimalField(label='Jumlah Tajaan',
                                         widget=forms.TextInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': 'Contoh: RM 50000.00',
                                             }
                                         ))

    NamaBank = forms.CharField(label='Nama Bank',
                                         widget=forms.TextInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': '',
                                             }
                                         ))

    NoAkaun = forms.CharField(label='No Akaun Bank',
                                         widget=forms.TextInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': '',
                                             }
                                         ))

    class Meta:
        model = models.Formzakat
        fields = ['title', 'icNo', 'body', 'poskod', 'bandar', 'noTel', 'DOB', 'tLahir', 'statusDiri', 'Kesihatan',
                  'ProgramPengajian', "Fakulti", "PeringkatPengajian", "TempohPengajian", "CPGA", "Penaja", "StatusPenaja", "JumlahTajaan",
                  "NamaBank", "NoAkaun",]
#        widgets = {
#            'title': forms.TextInput(attrs={'class': 'formzakat1'}),

#        }

#class RawApplyZakat(forms.Form):

#    title = forms.CharField(
#        label= 'Nama Penuh',
#        widget=forms.TextInput(
#            attrs={
#                "class": "formzakat1",
#                "rows": 10,
#                "cols": 100
#            }
#        )
#    )

#    icNo = forms.DecimalField(label='I/C No')


class DocZakat(forms.ModelForm):

    title = forms.CharField(label='Nama',
                                         widget=forms.TextInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': '',
                                             }
                                         ))

    icCopy = forms.CharField(label='Salinan Kad Pengenalan Pemohon',
                                         widget=forms.FileInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 #'placeholder': 'Contoh: 910121037659',
                                             }
                                         ))

    matricCopy = forms.CharField(label='Salinan Kad Matrik Pemohon',
                                         widget=forms.FileInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 #'placeholder': 'Contoh: 910121037659',
                                             }
                                         ))

    payslipCopy = forms.CharField(label='Salinan Penyata Gaji atau Surat Pengesahan Pendapatan',
                                         widget=forms.FileInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 #'placeholder': 'Contoh: 910121037659',
                                             }
                                         ))

    resultCopy = forms.CharField(label='Salinan Keputusan Pelajaran Terkini Pemohon',
                                         widget=forms.FileInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 #'placeholder': 'Contoh: 910121037659',
                                             }
                                         ))

    debtstateCopy = forms.CharField(label='Salinan Penyata Hutang', required=False,
                                         widget=forms.FileInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 #'placeholder': 'Contoh: 910121037659',
                                             }
                                         ))

    mualafCopy = forms.CharField(label='Salinan Pengesahan Mualaf', required=False,
                                         widget=forms.FileInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 #'placeholder': 'Contoh: 910121037659',
                                             }
                                         ))
    title = forms.CharField(label='Nama',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': '',
                                }
                            ))

    class Meta:
        model = models.Doczakat
        fields = ['title','icCopy', 'matricCopy', 'payslipCopy', 'resultCopy', 'debtstateCopy', 'mualafCopy']


class FamilyInfo(forms.ModelForm):

    NoKP = forms.CharField(label='No Kad Pengenalan ',
                                         widget=forms.TextInput(
                                             attrs={
                                                 'class': 'form-control',
                                                 'placeholder': 'Contoh: 910121037659',
                                             }
                                         ))

    TelNo = forms.CharField(label='No Telefon ',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Contoh: 0125932519',
                               }
                           ))

#    Hubungan = forms.CharField(label='Hubungan',
#                            widget=forms.RadioSelect(
#                                attrs={
#                                    'class': 'form-control',
#                                    'placeholder': 'Contoh: 0125932519',
#                                }
#                            ))

    Nama = forms.CharField(label='Nama Penjaga',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': '',
                                }
                            ))

#    Rumah = forms.CharField(label='Jenis Rumah',
#                           widget=forms.TextInput(
#                               attrs={
#                                   'class': 'form-control',
#                                   'placeholder': '',
#                               }
#                           ))

    PekerjaanPenjaga = forms.CharField(label='Pekerjaan Penjaga',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    PendapatanSebulan = forms.CharField(label='Pendapatan Sebulan',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    PekerjaanPasanagan = forms.CharField(label='Pekerjaan Pasangan',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    PendapatanSebulanPasangan = forms.DecimalField(label='Pendapatan Sebulan Pasangan',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    Pemohon = forms.DecimalField(label='Pemohon',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    PendapatanKeluarga = forms.DecimalField(label='Pendapatan Keluarga',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    SumbanganAnak = forms.DecimalField(label='Sumbangan Anak-Anak',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    SumbanganDana = forms.DecimalField(label='Sumbangan Dana',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    LainLain = forms.DecimalField(label='Sumbangan Lain-Lain',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '',
                               }
                           ))

    class Meta:
        model = models.Familyinfo
        fields = ['NoKP', 'TelNo', "Hubungan", "Nama", "Rumah", "PekerjaanPenjaga", "PendapatanSebulan","PekerjaanPasanagan","PendapatanSebulanPasangan",
                  "Pemohon", "PendapatanKeluarga", "SumbanganAnak", "SumbanganDana", "LainLain", ]


class ConfirmZakat(forms.ModelForm):

    title = forms.DecimalField(label='Email Pemohon',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   #'placeholder': '',
                               }
                           ))

    class Meta:
        model = models.Confirmzakat
        fields = ['title']



