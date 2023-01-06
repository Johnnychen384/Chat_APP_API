from django.contrib import admin

# Register your models here.
from .models import User, Buddy, Message
admin.site.register(User)
admin.site.register(Buddy)
admin.site.register(Message)
