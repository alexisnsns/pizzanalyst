from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin


from .models import Restaurant
from .models import Comment

admin.site.register(Restaurant)
admin.site.register(Comment)
