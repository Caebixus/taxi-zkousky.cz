from django.contrib import admin
from .models import TestText

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'question', 'correct', 'wrong1', 'wrong2')
    list_filter = ('tag', )
    search_fields = ('tag', 'question', 'correct', 'wrong1', 'wrong2')

# Register your models here.

admin.site.register(TestText, PostAdmin)
