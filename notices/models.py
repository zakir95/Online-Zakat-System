from django.db import models
from djchoices import DjangoChoices, ChoiceItem

# Create your models here.
class Notice(models.Model):

    class StatusApp(DjangoChoices):
        Lulus = ChoiceItem("lulus")
        Gagal = ChoiceItem("gagal")


    title = models.CharField(max_length=100)
    icNo = models.DecimalField(max_digits=12, decimal_places=0, default=None)
    status = models.CharField(max_length=10, choices=StatusApp.choices, default=None)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    #thumb = models.FileField(default='idefault.png', blank=True, null=True)

    # add in author later


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'