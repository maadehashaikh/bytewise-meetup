from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='all_meetups'),
    path('<slug:meetup_slug>',views.meetup_detail, name='meetup_details'),
    path('<slug:meetup_slug>/success/',views.confirm_registration, name='confirm-registration'),
]
