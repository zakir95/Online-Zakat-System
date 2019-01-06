from django.contrib import admin
from .models import Formzakat, Doczakat, Familyinfo #, Confirmzakat
from accounts import forms
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail


#def make_succeed(modeladmin, request, queryset):
#    queryset.update(status='p')
#make_succeed.short_description = "Mark selected applications as Succeed"

#class ZakatAdmin(admin.ModelAdmin):

#    actions = ['make_published']

#   list_display = ['title', 'status']
#    ordering = ['title']
#    actions = [make_succeed]

#    def make_succeed(self, request, queryset):
#        rows_updated = queryset.update(status='p')
#        if rows_updated == 1:
#            message_bit = "1 application was"
#        else:
#            user = get_user_model()
#            subject = 'Unit Zakat UNISEL'
#            message_bit = "%s applications were" % rows_updated
#            from_email = settings.EMAIL_HOST_USER
#            to_list = [user.email, settings.EMAIL_HOST_USER]
#            send_mail(subject, message_bit, from_email, to_list, fail_silently=True)
#        self.message_user(request, "%s Your Zakat Application ACCEPTED" % message_bit)

#def apply_upStatus(modeladmin, request, queryset):
#    user = get_user_model()
#    grab = {'user': request.user}


#    for confirmation in queryset:


#        confirmation.status = 'LULUS-ACCEPTED'

#        confirmation.save()
#        confirm.email = {'user': request.user}
#        subject = "Unit Zakat UNISEL"
#        from_email = settings.EMAIL_HOST_USER
#        to_email = [confirmation.title]
#        confirm_message = "Tahniah, permohonan Zakat UNISEL anda telah berjaya"
#        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=confirm_message,
#                  fail_silently=False)


#apply_upStatus.short_description = 'Tandakan sebagai LULUS'


#class ZakatAdmin(admin.ModelAdmin):
#    list_display = ['title', 'status']
#    actions = [apply_upStatus, ]



#def up_Status(modeladmin, request, queryset):
#    user = get_user_model()
#    grab = {'user': request.user}


#    for confirmation in queryset:


#        confirmation.status = 'LULUS-ACCEPTED'

#        confirmation.save()
#        confirm.email = {'user': request.user}
#        subject = "Zakat UNISEL Application Result"
#        from_email = settings.EMAIL_HOST_USER
#        to_email = [confirmation.title]
#        confirm_message = "Tahniah, permohonan Zakat UNISEL anda telah berjaya"
#        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=confirm_message,
#                  fail_silently=False)


#up_Status.short_description = 'Tandakan sebagai LULUS'


#class ConfirmAdmin(admin.ModelAdmin):
#    list_display = ['title', 'status']
#    actions = [up_Status, ]


class FamilyinfoTabularInline(admin.TabularInline):
    model = Familyinfo


class DoczakatTabularInline(admin.TabularInline):
    model = Doczakat


class FormzakatAdmin(admin.ModelAdmin):
    inlines = [FamilyinfoTabularInline, DoczakatTabularInline]
    class Meta:
        model = Formzakat



admin.site.register(Formzakat, FormzakatAdmin)

admin.site.register(Doczakat)

admin.site.register(Familyinfo)

#admin.site.register(Confirmzakat, ConfirmAdmin)

#admin.site.register(Dokzakat)

#admin.site.register(Agreeinfo)