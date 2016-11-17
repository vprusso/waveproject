import csv
import datetime

from .models import Document, DocumentEntry

def handle_files(csv_file):

    path = "C:/Users/Asus/Desktop/projects/" + csv_file.name
    fout = open(path, 'wb')
    for chunk in csv_file.chunks():
        fout.write(chunk)
    fout.close()

    newdoc = Document(docfile=path)
    newdoc.save()

    reader = csv.DictReader(open(path))
    for row in reader:        
        date = sanitize_date_format(row['date'])
        category = row['category']
        employee_name = row['employee name']
        employee_address = row['employee address']
        expense_description = row['expense description']
        pre_tax_amount = sanitize_float_format(row['pre-tax amount'])
        tax_name = row['tax name']
        tax_amount = sanitize_float_format(row['tax amount'])

        entry = DocumentEntry(
            document=newdoc, date=date, 
            category=category, employee_name=employee_name,
            employee_address=employee_address, expense_description=expense_description,
            pre_tax_amount=pre_tax_amount, tax_name=tax_name,
            tax_amount=tax_amount
            )
        entry.save()
    

def sanitize_date_format(date):
    # TODO (more date checking here....)
    return datetime.datetime.strptime(date, "%m/%d/%Y").strftime('%Y-%m-%d')

def sanitize_float_format(str_float_val):
    # TODO (more checking here...)
    return str_float_val.replace(',','')