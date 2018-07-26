from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout, login
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import render
from django.urls import reverse


def logout_view(request):
    """Log the account out."""
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))


def register(request):
    """Register a new account."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the account in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('account:login'))
    context = {'form': form}
    return render(request, 'account/register.html', context)
