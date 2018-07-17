from django.db import models
from django.utils import timezone

#these are for validating errors
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

#validate a number is divisable by 3  
#TODO: Add more descriptive text 
def validate_div3(value):
    if value % 3 != 0:
        raise ValidationError(
            _('%(value)s is not divisable by 3.'),
            params={'value': value},
        )
#Checks the database to see if there is an existing record with the same name
def validateUniqueName(value):
	lookup = Entry.objects.filter(name=value).exists()
	if lookup == True:
		raise ValidationError(
			_('We are sorry, but "%(value)s" has already been registered.  Please pick a different name for your number.'),
			params={'value': value},
			)
#Checks the database to see if the number has been registered.
def validateUniqueNumber(value):
	lookup = Entry.objects.filter(number=value).exists()
	if lookup == True:
		raise ValidationError(
			_('We are sorry, but "%(value)s" has already been registered.  Please pick a different number to register.  Luckily, you have an infinite number to choose from!'),
			params={'value': value},
			)

# Model for Adding a new number to the dictoinary
class Entry(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, validators=[validateUniqueName])
    number = models.BigIntegerField(validators=[validate_div3, validateUniqueNumber])
    comment = models.TextField(blank=True)
    dedication = models.CharField(blank=True, max_length=100)
    created_date = models.DateTimeField(
            default=timezone.now)
    famous = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

#Model for user's carts
class Cart(models.Model):
	buyer = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	desiredname = models.CharField(max_length=100, validators=[validateUniqueName])
	desirednumber = models.BigIntegerField(validators=[validate_div3, validateUniqueNumber])
	desiredcomment = models.TextField(blank=True)
	desireddedication = models.CharField(blank=True, max_length=100)
	created_date = models.DateTimeField(
            default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
