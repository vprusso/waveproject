from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document, DocumentEntry
from .forms import UploadFileForm
from .file_handler import save_file_content_to_database, calculate_total_expenses_per_month


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
    calculate_total_expenses_per_month()

    # Render list page with the documents and the form
    return render(
        request,
        'upload/list_files.html',
        {'documents': documents, 'document_entries':document_entries, 'form': form}
    )
