from django.contrib import admin
from .models import Image  # Ensure your model is imported

class ImageAdmin(admin.ModelAdmin):  # Use ModelAdmin here
    list_display = ('id','photo', 'date')  # Customize as needed

admin.site.register(Image, ImageAdmin)
