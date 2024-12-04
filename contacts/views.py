from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponseRedirect
from django.contrib import messages

 
def success(request):
    return render(request, 'contacts/success.html')


def home(request):
        contacts = Contact.objects.all()
        return render(request, 'contacts/home.html', {'contacts': contacts})
    
    
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            name = formdata['name']
            address = formdata['address']
            profession = formdata['profession']
            tel_number = formdata['tel_number']
            email_address = formdata['email_address']
            new_contact = Contact.objects.create(name=name, address=address,  profession=profession, tel_number=tel_number, email_address=email_address)
            messages.success(request, 'Success! Your contact has been added.')
            return HttpResponseRedirect(reverse('home') + f'?new_contact_pk={new_contact.pk}&success=1')
    else:
        form = ContactForm()  
        return render(request, 'contacts/contact_create.html', {'form':form})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_edit.html', {'form': form, 'contact': contact})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})