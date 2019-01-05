from django.db import models
from django.contrib.auth.models import User
from djchoices import DjangoChoices, ChoiceItem
from datetimepicker.widgets import DateTimePicker
from django import forms



# Create your models here.
class Formzakat(models.Model):
    class StatusKahwin(DjangoChoices):
        Bujang = ChoiceItem("bujang")
        Berkahwin = ChoiceItem("berkahwin")
        Duda = ChoiceItem("duda")
        Janda = ChoiceItem("janda")

    class StatusFizikal(DjangoChoices):
        Sihat = ChoiceItem("sihat")
        Sakit = ChoiceItem("sakit")
        OKU = ChoiceItem("oku")

    class faculty(DjangoChoices):
        CVAC = ChoiceItem("cvac")
        ELS = ChoiceItem("els")
        FESS = ChoiceItem("fess")
        FOB = ChoiceItem("fob")
        CFGS = ChoiceItem("cfgs")
        CGS = ChoiceItem("cgs")

    class lvlStudy(DjangoChoices):
        Asasi = ChoiceItem("asasi")
        Diploma = ChoiceItem("diploma")
        Ijazah = ChoiceItem("degree")
        Sarjana = ChoiceItem("master")
        PHD = ChoiceItem("phd")

    class sponsor(DjangoChoices):
        SedangDipohon = ChoiceItem("ongoing")
        SedangMenerima = ChoiceItem("received")
        Tamat = ChoiceItem("finished")
        Digantung = ChoiceItem("suspended")









    # Maklumat Diri

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    icNo = models.DecimalField(max_digits=12, decimal_places=0, default=None)
    body = models.TextField()
    poskod = models.DecimalField(max_digits=5, decimal_places=0, default=None)
    bandar = models.CharField(max_length=20, default=None)
    noTel = models.DecimalField(max_digits=11, decimal_places=0, default=None)
    DOB = models.CharField(max_length=20, default=None)
    tLahir = models.CharField(max_length=20, default=None)
    statusDiri = models.CharField(max_length=10, choices=StatusKahwin.choices, default=None)
    Kesihatan = models.CharField(max_length=10, choices=StatusFizikal.choices, default=None)

    date = models.DateTimeField(auto_now_add=True)
#    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, blank=False, default=None, on_delete=models.CASCADE)

    # Maklumat Pengajian
    ProgramPengajian = models.CharField(max_length=100, default=None)
    Fakulti = models.CharField(max_length=10, choices=faculty.choices, default=None)
    PeringkatPengajian = models.CharField(max_length=10, choices=lvlStudy.choices, default=None)
    TempohPengajian = models.DecimalField(max_digits=2, decimal_places=1, default=None)
    #Semester = models.AutoField(default=None)
    CPGA = models.DecimalField(max_digits=3, decimal_places=2, default=None)
    Penaja = models.CharField(max_length=100, default=None)
    StatusPenaja = models.CharField(max_length=15, choices=sponsor.choices, default=None)
    JumlahTajaan = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    NamaBank = models.CharField(max_length=100, default=None)
    NoAkaun = models.CharField(max_length=30, default=None)

#    yourEmail = models.CharField(max_length=100, default=None, null=False)





class Doczakat(models.Model):
    # Zakat Document Needed
    title = models.CharField(max_length=30, default=None, null=True)
    icCopy = models.FileField(blank=True, null=True)
    matricCopy = models.FileField(blank=True, null=True)
    payslipCopy = models.FileField(blank=True, null=True)
    resultCopy = models.FileField(blank=True, null=True)
    debtstateCopy = models.FileField(blank=True, null=True)
    mualafCopy = models.FileField(blank=True, null=True)
    author = models.ForeignKey(Formzakat, blank=False, default=None, on_delete=models.CASCADE, related_name='+')

class Familyinfo(models.Model):
    # Maklumat IbuBapa
    class relation(DjangoChoices):
        Bapa = ChoiceItem("father")
        Ibu = ChoiceItem("mum")
        BapaTiri = ChoiceItem("stepFather")
        IbuTiri = ChoiceItem("stepMum")
        Datuk = ChoiceItem("gFather")
        Nenek = ChoiceItem("gMother")
        Penjaga = ChoiceItem("guardian")

    class house(DjangoChoices):
        SENDIRI = ChoiceItem("sendiri")
        SEWA = ChoiceItem("sewa")

    NoKP = models.DecimalField(max_digits=12, decimal_places=0, default=None)
    TelNo = models.DecimalField(max_digits=11, decimal_places=0, default=None)
    Hubungan = models.CharField(max_length=10, choices=relation.choices, default=None)
    Nama = models.CharField(max_length=100, default=None)

    Rumah = models.CharField(max_length=10, choices=house.choices, default=None)
    PekerjaanPenjaga = models.CharField(max_length=100, default=None)
    PendapatanSebulan = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    PekerjaanPasanagan = models.CharField(max_length=100, default=None)
    PendapatanSebulanPasangan = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    Pemohon = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    PendapatanKeluarga = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    SumbanganAnak = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    SumbanganDana = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    LainLain = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    author = models.ForeignKey(Formzakat, blank=False, default=None, on_delete=models.CASCADE)

class Confirmzakat(models.Model):

    class StatusKini(DjangoChoices):
        Lulus = ChoiceItem("LULUS")
        Gagal = ChoiceItem("GAGAL")

    title = models.CharField(max_length=50, default=None)
    #emailku = models.CharField(max_length=50, default=None)
    status = models.CharField(max_length=10, choices=StatusKini.choices, default=None, null=True)

    class Meta:
        verbose_name = 'confirmation'




    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'