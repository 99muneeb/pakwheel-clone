from pages.models import Team
from django.contrib import admin
from django.utils.html import  format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.image.url))
    thumbnail.short_description='Photo'
    list_display=('id','thumbnail','FirstName' ,'LastName','Designation','date')
    list_display_links=('id','FirstName')
    search_fields=('FirstName','Designation')
    list_filter=('Designation',)
# Register your models here.
admin.site.register(Team, TeamAdmin)

