from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About

# Important to register any app/model with Summernote
# [ if SummerNote is installed for Admin panel ]
# decorator is how to register a class,
# compared to just registering the standard model
# decorator is more Pythonic and allows customising the
# registered models how they will appear on the admin site
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    Lists fields for display in admin, fileds for search
    and rich-text editor.
    """

    summernote_fields = ('content',)
