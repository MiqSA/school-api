from django.contrib import admin
from school.models import Student, Class, Subscription



class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birthday')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)



class Classes(admin.ModelAdmin):
    list_display = ('id', 'code_class', 'description')
    list_display_links = ('id', 'code_class')
    search_fields = ('code_class',)

admin.site.register(Class, Classes)



class Subscriptions(admin.ModelAdmin):
    list_display = ('id', 'student', 'class_name', 'period')
    list_display_links = ('id',)

admin.site.register(Subscription, Subscriptions)