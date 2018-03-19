from django.contrib import admin
from .models import Blog, Comments,Profile

# Register your models here.
admin.site.register(Blog)
admin.site.register(Comments)
admin.site.register(Profile)