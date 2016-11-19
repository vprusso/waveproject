from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from chartit import DataPool, Chart

from .models import Document, MonthlyExpenditure
from .forms import UploadFileForm
from .file_handler import save_file_content_to_database, calculate_total_expenses_per_month, save_total_monthly_expenses_to_database
from .utils import month_name


def list_files(request):

    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            save_file_content_to_database(request.FILES['docfile'])

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list_files'))
    else:
        form = UploadFileForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    monthly_expenses = calculate_total_expenses_per_month()
    # TODO UNCOMMENT
    save_total_monthly_expenses_to_database(monthly_expenses)            

    #Step 1: Create a DataPool with the data we want to retrieve.
    # start_code
    ds = DataPool(
        series=[{
            'options': {
                'source': MonthlyExpenditure.objects.all()
            },
            'terms': [
                'year',
                'monthly_expenditure',
                'month',
            ]
        }]
    )

    cht = Chart(
        datasource=ds,
        series_options=[{
            'options': {
                'type': 'pie',
                'stacking': False
            },
            'terms': {
                'month': ['monthly_expenditure'],
            }
        }],
        chart_options={
            'title': {
                'text': 'Total expenditures per month (over all years)'
            }
        },
        x_sortf_mapf_mts=(None, month_name, False)
    )

    # Render list page with the documents and the form
    return render(
        request,
        'upload/list_files.html',
        {'documents': documents, 'monthly_expenses': monthly_expenses,
         'form': form, 'expensechart': cht}
    )


# TODO Have another form do work for chartting...