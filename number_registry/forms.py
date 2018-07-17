from django import forms
from .models import Entry

#these are for validating errors
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _




class Reserve(forms.ModelForm):	
	class Meta:
		model = Entry
		fields = ('name', 'number', 'comment', 'dedication',)


"""		
	name = forms.CharField(max_length=100)
	number = forms.IntegerField(validators=[validate_div3])
	comment = forms.CharField(required=False)
	dedication = forms.CharField(required=False, max_length=100)
"""

"""
TODO:
For Validation of unique values:

https://docs.djangoproject.com/en/2.0/ref/forms/validation/
The clean_<fieldname>() method is called on a form subclass – where <fieldname> is replaced with the name of the form field attribute. This method does any cleaning that is specific to that particular attribute, unrelated to the type of field that it is. This method is not passed any parameters. You will need to look up the value of the field in self.cleaned_data and remember that it will be a Python object at this point, not the original string submitted in the form (it will be in cleaned_data because the general field clean() method, above, has already cleaned the data once).

For example, if you wanted to validate that the contents of a CharField called serialnumber was unique, clean_serialnumber() would be the right place to do this. You don’t need a specific field (it’s just a CharField), but you want a formfield-specific piece of validation and, possibly, cleaning/normalizing the data.

This is the validation for divisible by 3.  SHouldn't be needed here, since I have it on the model.
def validate_div3(value):
    if value % 3 != 0:
        raise ValidationError(
            _('%(value)s is not divisable by 3.'),
            params={'value': value},
        )

"""