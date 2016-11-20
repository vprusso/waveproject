from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from chartit import DataPool, Chart

from .models import Document, MonthlyExpenditure
from .forms import UploadFileForm, SelectYearForm
from .file_handler import save_file_content_to_database, calculate_total_expenses_per_month, save_total_monthly_expenses_to_database
from .utils import DateHelper


def list_files(request):

    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            save_file_content_to_database(request.FILES['docfile'])
            monthly_expenses = calculate_total_expenses_per_month()
            save_total_monthly_expenses_to_database(monthly_expenses)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list_files'))
    else:
        form = UploadFileForm()  # A empty, unbound form

    # Year form
    year = None

    if request.method == "POST":
        year = request.POST['year']
        year_form = SelectYearForm(request.POST)
        if year_form.is_valid():
            year = request.POST['year']
    else:

        year_form = SelectYearForm()

    # Load documents for the list page
    documents = Document.objects.all()
    date_helper = DateHelper()

    monthly_expenses = calculate_total_expenses_per_month()

    # Step 1: Create a DataPool with the data we want to retrieve.
    ds = DataPool(
        series=[{
            'options': {
                'source': MonthlyExpenditure.objects.all().filter(year=year)
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
                'text': 'Total expenditures per month for ' + str(year)
            }
        },
        x_sortf_mapf_mts=(None, date_helper.month_name, False)
    )

    ms = MonthlyExpenditure.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'upload/list_files.html',
        {'documents': documents, 'monthly_expenses': monthly_expenses,
         'form': form, 'expensechart': cht, 'ms': ms, 'year_form': year_form}
    )
