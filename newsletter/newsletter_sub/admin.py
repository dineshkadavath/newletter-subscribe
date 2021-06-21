from django.contrib import admin
print("hii")
# Register your models here.
from .models import Newsletter

print("hii 222")
admin.site.register(Newsletter)
print("hii 333")