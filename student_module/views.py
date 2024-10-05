from django.shortcuts import render, redirect
from .forms import StudentForm, StudentProfileForm, StudentPermanentAddressForm, StudentTempAddressForm

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
        else:
            print(form.errors)
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})

def student_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentProfileForm()

    return render(request, 'students/student_profileform.html', {'form': form})

def student_permanent_address_view(request):
    if request.method == 'POST':
        form = StudentPermanentAddressForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentPermanentAddressForm()

    return render(request, 'students/student_permanent_address_form.html', {'form': form})

def student_temp_address_view(request):
    if request.method == 'POST':
        form = StudentTempAddressForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = StudentTempAddressForm()

    return render(request, 'students/student_temp_address_form.html', {'form': form})