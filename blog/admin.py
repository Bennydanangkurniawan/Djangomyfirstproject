from django.contrib import admin

from  . import models

# from django_markdown.admin import MarkdownModelAdmin
# Register your models here.
class EntryAdmin(admin.ModelAdmin):
	list_display = ("title" , "created")
	prepopulated_fields={"slug" : ("title",)}



# container 
admin.site.register(models.Entry, EntryAdmin)

# Portofolio
admin.site.register(models.Portofolio,EntryAdmin)

# Slider
admin.site.register(models.Slider)




