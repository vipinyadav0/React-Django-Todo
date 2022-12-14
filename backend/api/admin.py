from django.contrib import admin
from .models import (
                    Student, Family, Todo
)


class FamilyInline(admin.StackedInline):
    model = Family
    extra = 0

class StudentInline(admin.ModelAdmin):
    inlines = [FamilyInline,]

class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ['id','title', 'description', 'completed']
admin.site.register(Student, StudentInline)

admin.site.register(Family)
admin.site.register(Todo, TodoAdmin)

