from django.contrib import admin
from .models import *

@admin.register(email_send)
class email_sendAdmin(admin.ModelAdmin):
    list_display = ['email_to','email_from','email_sub','email_attachment']
