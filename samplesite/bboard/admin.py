from django.contrib import admin


from .models import Bb
from .models import Rubric

admin.site.register(Rubric)


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric','phone','named')
    list_display_links = ('title', 'content','price')
    search_fields = ('title', 'content','price')


admin.site.register(Bb, BbAdmin)
