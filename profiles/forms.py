from django import forms
from profiles.widgets import CustomClearableFileInput
from .models import User,  UserProfile


class UserProfileForm(forms.ModelForm):
    # birthdate = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    weight = forms.DecimalField(widget=forms.NumberInput(attrs={'max': '250'}))
    class Meta:
        model = UserProfile
        fields = ('full_name', 'town_or_city', 'country',
                  'gender', 'weight', 'image')  # 'birthdate',

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'town_or_city': 'Town or City',
            'gender': 'Gender',
            'weight': 'weight in kilograms',
            # 'birthdate': 'Date of birth: dd-mm-yyyy'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country' and field != 'image':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
            self.fields[field].label = False
