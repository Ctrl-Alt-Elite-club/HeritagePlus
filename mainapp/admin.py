from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([City,User,Monument,Report,MonumentImage,ReportImage])

