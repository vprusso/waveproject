from django.contrib import admin
from .models import Document, DocumentEntry, MonthlyExpenditures

admin.site.register(Document)
admin.site.register(DocumentEntry)
admin.site.register(MonthlyExpenditures)
