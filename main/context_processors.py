from . forms import AppointmentMForm

def appointment_form(request):
    return {"appointment_form": AppointmentMForm()}