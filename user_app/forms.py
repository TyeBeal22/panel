from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUserProfile, Stock



class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, label='First Name', help_text='First Name', required=True)
    last_name = forms.CharField(max_length=50, label='Last Name', help_text='Last Name', required=True)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user


class UpdateProfileForm(forms.ModelForm):
    """ update user profile."""

    class Meta:
        model = CustomUserProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'country',
            'occupation', 'phone_number', 'photo']



class StockCreateForm(forms.ModelForm):
    class Meta:
        model= Stock
        fields = ['category', 'item_name', 'quantity']