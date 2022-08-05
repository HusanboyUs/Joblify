from django.contrib import admin
from base.models import Jobs, User


admin.site.register(User)

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display=('company','job_type')