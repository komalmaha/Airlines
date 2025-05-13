from django.contrib import admin
from service.models import Signup,Flight,reservation
# Register your models here.
admin.site.register(Signup)
admin.site.register(Flight)
admin.site.register(reservation)
