from django.urls import path
from .views import (
    RegisterView,
    CancelRegistrationView,
    ListRegistrationsView,
    register_form,
    registration_list,
    cancel_form,
)

app_name = 'registration'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('cancel/', CancelRegistrationView.as_view(), name='cancel_registration'),
    path('list/', ListRegistrationsView.as_view(), name='registration_list'),
    path('register_form/', register_form, name='register_form'),
    path('', registration_list, name='registration_list'),
    path('cancel-form/', cancel_form, name='cancel_form'),
]
