from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Entry
from .forms import Reserve



def entry_list(request):
	entries = Entry.objects.order_by('number')
	return render(request, 'number_registry/entry_list.html', {'entries':entries})

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


""" 
This was my old one, based on the Mozilla tutorial
def reserve(request):
	new_reservation = reserve(initial={'name':name})
	# If this is a POST request then process the Form data
	if request.method == 'POST':
		# Create a form instance and populate it with data from the request (binding):
	 	form = ReserveNewNumber(request.POST)
	 	
	 	# Check if the form is valid:
	 	if form.is_valid():
	 		new_reservation = form.clean_number()
	 		new_reservation = form.clean_name()

	return render(request, 'number_registry/reserve_number.html', {'form':form, 'new_reservation':new_reservation})
	"""