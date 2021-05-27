from django.contrib import admin
from todo.models import TODO
from .models import CR
# Register your models here.
admin.site.register(TODO)
admin.site.register(CR)