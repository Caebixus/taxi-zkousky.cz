from django.contrib import admin
from quiz import views
from .models import Feedback

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('feedbackUser', 'message', 'message_published',)
    list_filter = ('message_published', )

# Register your models here.

admin.site.register(Feedback, ContactAdmin)
