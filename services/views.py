from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Service, ServiceRequest
from .forms import CreateNewService, RequestServiceForm
from users.models import Company, Customer, User

def service_list(request):
    # Get query parameters for filtering and sorting
    field = request.GET.get('field', None)  # Filter by field
    sort_by = request.GET.get('sort_by', None)  # Sort options: 'popularity' or 'date'

    # Queryset for services
    services = Service.objects.all()

    # Apply filtering
    if field:
        services = services.filter(field=field)

    # Apply sorting
    if sort_by == 'popularity':
        services = services.annotate(request_count=Count('servicerequest')).order_by('-request_count')
    else:  # Default: Sort by most recent
        services = services.order_by('-date_created')

    # Fetch unique fields for filtering options in the template
    fields = Service.objects.values_list('field', flat=True).distinct()

    return render(request, 'services/service_list.html', {
        'services': services,
        'fields': fields,
        'current_field': field,
        'current_sort': sort_by,
    })

def most_requested_services(request):
    services = Service.objects.annotate(request_count=Count('servicerequest')).order_by('-request_count')[:10]
    return render(request, 'services/most_requested_services.html', {'services': services})

@login_required
def create(request):
    #Check if the user is a company
    if request.user.is_customer:
        #Prevent customers from accessing the services cfreation page
        messages.error(request, 'You must be a company to create a service.')
        return redirect('users:customer_profile', username=request.user.username)
    if request.method == 'POST':
        form = CreateNewService(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            #Check if the service's field matches the company's field
            if request.user.company.field != 'All in One' and service.field != request.user.company.field:
                messages.error(request, 'You can only create services in your field of work.')
                return redirect('services:service_create')
            #Assign the company to the service and save
            service.company = request.user.company
            service.save()
            messages.success(request, 'Service created successfully.')
            return redirect('services:service_list')
    else:
        form = CreateNewService()
    return render(request, 'services/service_create.html', {'form': form})

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    company=service.company # get the company that created the service
    return render(request, 'services/service_detail.html', {'service': service, 'company': company})

@login_required
def request_service(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.service = service
            service_request.save()
            messages.success(request, 'Service requested successfully.')
            return redirect('services:service_list')
    else:
        form = RequestServiceForm()
    return render(request, 'services/request_service_form.html', {'form': form, 'service': service})

def service_field(request, field):
    services = Service.objects.filter(field=field).order_by('-date_created')
    return render(request, 'services/service_field.html', {'services': services, 'field': field})

@login_required
def company_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Company, user=user) #Get the company profile
    services = Service.objects.filter(company=profile)#Get services created by the company
    return render(request, 'users/company_profile.html', {
        'user': user,
        'profile': profile,
        'services': services
    })

@login_required
def customer_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Customer, user=user)
    available_services = Service.objects.all()
    requested_services = ServiceRequest.objects.filter(customer=profile)
    return render(request, 'users/customer_profile.html', {
        'user': user,
        'profile': profile,
        'available_services': available_services,
        'requested_services': requested_services
    })