from django.shortcuts import render, redirect
from .models import *
from .forms import ReservationForm, ContactUsForm
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='account/login/')
def main(request):
    if request.method == 'POST':
        form_reserve = ReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    
    
    if request.method == 'POST':
        form_contact = ContactUsForm(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect('/')
    
    


    heroes = Hero.objects.all()
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    specials = Dish.objects.filter(is_special=True)
    form_reserve = ReservationForm()
    abouts = About.objects.all()
    staff = Staff.objects.all()
    galleries = Gallery.objects.all()
    whyus = WhyUs.objects.all()
    testimonials = Testimonial.objects.all()
    contacts = Contacts.objects.all()
    events = Event.objects.all()
    form_contact = ContactUsForm()


    return render(request, 'core/main.html', context={
        'heroes': heroes,
        'abouts': abouts,
        'whyus': whyus,
        'categories': categories,
        'dishes': dishes,
        'specials': specials,
        'events' : events,
        'form_reserve': form_reserve,
        'staff': staff,
        'galleries': galleries,
        'testimonials': testimonials,
        'contacts': contacts,
        'form_contact': form_contact,
    })


# Checking if user is a "Manager"
def is_manager(user):
    return user.groups.filter(name='manager').exists()

# If user is a manager: give access to reservations list page
@login_required(login_url='account/login/')
@user_passes_test(is_manager)
def list_reservations(request):
    messages = Reservation.objects.filter(is_processed=False)
    return render(request, 'core/reservations.html', context={'reservations': messages})

# If user is a manager: give access to reservations list editing
@login_required(login_url='users/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    Reservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('core/list_reservations')

