from django.contrib import admin
from .models import Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'done') #какие поля моделей мы будем видеть в списке
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')#по каким полям моделей мы можем искать
    list_editable = ('done',)#что можем модифицировать
    list_filter = ('done',)#как можем фильтровать список нашей модели


admin.site.register(Todo, TodoAdmin)