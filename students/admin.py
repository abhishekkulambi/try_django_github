from django.contrib import admin
from .models import StudentInfo, StudentAcademics

# Register your models here.
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ["roll_no", "name"]
    search_fields = ["roll_no", "name"]

class StudacademicsAdmin(admin.ModelAdmin):
    list_display = ["roll_no",]
    


admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(StudentAcademics, StudacademicsAdmin)

