from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Meetup,Participant
from . forms import Registrations


# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetup/index.html', {
        "meetups": meetups
    })


def meetup_detail(request, meetup_slug):
    
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
       
        if request.method=='GET':
            Registration_form = Registrations()
            
        else:
            Registration_form= Registrations(request.POST)
            if Registration_form.is_valid():
                user_email = Registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)     
                # Participant= Registration_form.save()
                # selected_meetup.participants.add(participant)
                return redirect('confirm-registration',meetup_slug=meetup_slug)
        return render(request, 'meetup/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': Registration_form
            })

    except Exception as exc:
        print(exc)
        return render(request, 'meetup/meetup-details.html', {
            'meetup_found': False

        })


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetup/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })