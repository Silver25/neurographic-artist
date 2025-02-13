from django.contrib import admin
from .models import About

# Important to register any app/model with Summernote
# [ if SummerNote is installed for Admin panel ]
admin.site.register(About)