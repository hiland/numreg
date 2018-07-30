from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import Entry, Cart
from .forms import Reserve, SignUpForm, ReserveCart

# This is the homepage
def index(request):
	return render(request, 'number_registry/index.html')

# Lists all known entries.  (for now)
def entry_list(request):
	entries = Entry.objects.order_by('number')
	return render(request, 'number_registry/entry_list.html', {'entries':entries})

# Creates a new reservation.  NOTE:  This needs to write to the cart and not the registry!
#Will need to be depricated!
def reserve_new(request):
	if request.method == "POST":
		form = Reserve(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.owner = request.user
			post.save()
			return redirect('entry_list')
	else:
		form = Reserve()

	return render(request, 'number_registry/reserve_number.html', {'form': form})

#Adding reservations to the cart
def reserve_cart(request):
	if request.method == "POST":
		form = ReserveCart(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.buyer = request.user
			post.save()
			return redirect('review_cart')
	else:
		form = ReserveCart()

	return render(request, 'number_registry/reserve_cart.html', {'form': form})

# Shows cart items to user
@login_required
def review_cart(request):
		cartContents = Cart.objects.filter(buyer_id=request.user)
		return render(request, 'number_registry/review_cart.html', {'cartContents':cartContents})


# New User creation page.  Facebook login works!
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'number_registry/signup.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('/')


@login_required
def home(request):
    return render(request, 'number_registry/home.html')



