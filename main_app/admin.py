from django.contrib import admin
from .models import Finch, Feeding

# Register your models here.
admin.site.register(Finch)

# register feeding model here
admin.site.register(Feeding)
