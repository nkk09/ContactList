from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponseRedirect
from django.contrib import messages
from recommendation.recom_engine import search_contacts
 
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
            user_id = formdata['user_id']
            first_name = formdata['first_name']
            last_name = formdata['last_name']
            sex = formdata['sex']
            email = formdata['email']
            phone = formdata['phone']
            date_of_birth = formdata['date_of_birth']
            job_title = formdata['job_title']
            city = formdata['city']
            country = formdata['country']
            address = formdata['address']
            fees = formdata['fees']
            combined = formdata['combined']
            
            new_contact = Contact.objects.create(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                email=email,
                phone=phone,
                date_of_birth=date_of_birth,
                job_title=job_title,
                city=city,
                country=country,
                address=address,
                fees=fees,
                combined=combined
            )
            messages.success(request, 'Success! Your contact has been added.')
            return HttpResponseRedirect(reverse('home') + f'?new_contact_pk={new_contact.pk}&success=1')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_create.html', {'form': form})


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


def recommend_contacts(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        recommended_contacts = search_contacts(prompt)
        return render(request, 'contacts/home.html', {'contacts': recommended_contacts})
    return render(request, 'contacts/home.html', {'contacts': Contact.objects.all()})