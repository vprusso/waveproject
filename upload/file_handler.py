import csv
import dateutil.parser
import collections
import os

from .models import Document, DocumentEntry, MonthlyExpenditure
from . import utils

def save_file_content_to_database(csv_file):

    # TODO change this path to not be hardcoded
    path = os.getcwd() + r'/' + csv_file.name
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
    return dateutil.parser.parse(date).strftime('%Y-%m-%d')
    

def sanitize_float_format(str_float_val):
    # TODO (more checking here...)

    str_float_val = str_float_val.replace(',', '')
    str_float_val = dollars_to_cents(str_float_val)

    return str_float_val


def dollars_to_cents(dollars, truncate=True):
    cents = float(dollars) * 100
    if truncate:
        return int(cents)
    else:
        return cents


def cents_to_dollars(cents):
    return format(float(cents) / 100.0, '.2f')


def calculate_total_expenses_per_month():
    """ """
    year_month_dict = {}
    for instance in DocumentEntry.objects.all():
        year_month = str(instance.date.year) + "-" + str('%02d' % instance.date.month) 

        if year_month not in year_month_dict:
            year_month_dict[year_month] = instance.tax_amount + instance.pre_tax_amount

        else:
            year_month_dict[year_month] += instance.tax_amount + instance.pre_tax_amount

    # The costs are stored in terms of cents instead of dollars to eliminate floating
    # point accuracy issues. We then need to convert back to dollars. 
    year_month_dict = {k: cents_to_dollars(v) for k, v in year_month_dict.items()}        

    # Order in reverse chronological order
    year_month_dict = collections.OrderedDict(sorted(year_month_dict.items()))

    return year_month_dict


def save_total_monthly_expenses_to_database(monthly_expenses):
    for key, value in monthly_expenses.items():
        
        year_month_split = key.split("-")        
        year = year_month_split[0]
        month = year_month_split[1]

        expense = MonthlyExpenditure(
            month=month, year=year,
            monthly_expenditure=value
        )    
        expense.save()
