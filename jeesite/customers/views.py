from django.shortcuts import redirect, render
from .forms import CustomerSignupForm
from .models import Customer
def signup(request):
    customer=None
    if request.method == 'POST':
        forms= CustomerSignupForm(request.POST)
        if forms.is_valid():
           forms.save()
        customer=Customer.objects.all()
        return render(request, 'customers/customer_details.html', {'customer'})
    else:
         forms =CustomerSignupForm()
    return render(request,'customers/signup.html',{'forms':forms,'customer':customer})
# Create your views here.