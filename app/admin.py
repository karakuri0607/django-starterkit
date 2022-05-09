from django.contrib import admin
from .models import m_category, m_tag, t_table
from django_summernote.admin import SummernoteModelAdmin

class AppAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(m_category)
admin.site.register(m_tag) 
admin.site.register(t_table, AppAdmin)
