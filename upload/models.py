from django.db import models
from datetime import datetime, date

import os


class Document(models.Model):
    docfile = models.FileField(upload_to='documents')

    def get_filename(self):
        return os.path.basename(self.docfile.name)
   

class DocumentEntry(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    category = models.CharField(max_length=250, default=None)
    employee_name = models.CharField(max_length=250, default=None)
    employee_address = models.CharField(max_length=250, default=None)
    expense_description = models.CharField(max_length=500, default=None)
    pre_tax_amount = models.FloatField(default=None)
    tax_name = models.CharField(max_length=250, default=None)
    tax_amount = models.FloatField(default=None)