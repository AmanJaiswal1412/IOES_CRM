from django.shortcuts import render, redirect
from .forms import AcademicsForm, DocumentForm, ApplicationStatusForm

def academics_view(request):
    if request.method == 'POST':
        form = AcademicsForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AcademicsForm()

    return render(request, 'application/academics_form.html', {'form': form})

def document_upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = DocumentForm()

    return render(request, 'application/document_form.html', {'form': form})

def application_status_view(request):
    if request.method == 'POST':
        form = ApplicationStatusForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ApplicationStatusForm()

    return render(request, 'application/application_status_form.html', {'form': form})