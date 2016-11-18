from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from chartit import DataPool, Chart

from .models import Document, DocumentEntry, MonthlyExpenditures
from .forms import UploadFileForm
from .file_handler import save_file_content_to_database, calculate_total_expenses_per_month, save_total_monthly_expenses_to_database

def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names[month_num]


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
    document_entries = DocumentEntry.objects.all()
    
    monthly_expenses = calculate_total_expenses_per_month()
    #save_total_monthly_expenses_to_database(monthly_expenses)

    #Step 1: Create a DataPool with the data we want to retrieve.
    # start_code
    ds = DataPool(
            series=[{
                'options': {
                    'source': MonthlyExpenditures.objects.filter(year=2013)
                },
                'terms': [
                    'month',
                    'monthly_expenditure'
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
                    'month': ['monthly_expenditure']
                }
            }],
            chart_options={
                'title': {
                    'text': 'Monthly Temperature of Boston'
                }
            },
            x_sortf_mapf_mts=(None, monthname, False)
    )


    # Render list page with the documents and the form
    return render(
        request,
        'upload/list_files.html',
        {'documents': documents, 'document_entries':document_entries, 
         'monthly_expenses': monthly_expenses, 'form': form, 'weatherchart':cht}
    )
