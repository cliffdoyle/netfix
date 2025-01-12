from django import forms
from .models import Service, ServiceRequest,ServiceRating

class CreateNewService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price_hour', 'field']

    def __init__(self, *args, **kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)
        # adding placeholders to form fields
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'
        self.fields['name'].widget.attrs['autocomplete'] = 'off'

class RequestServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['address', 'service_time']

    def __init__(self, *args, **kwargs):
        super(RequestServiceForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['placeholder'] = 'Enter Address'
        self.fields['service_time'].widget.attrs['placeholder'] = 'Enter Service Time (hours)'
        
class ServiceRatingForm(forms.ModelForm):
    class Meta:
        model = ServiceRating
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),  # Display radio buttons for ratings
        }