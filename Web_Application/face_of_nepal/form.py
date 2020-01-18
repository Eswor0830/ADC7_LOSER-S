from django import forms
from .models import Freelancer


class FreelancerForm(forms.ModelForm):

    class Meta:
        model = Freelancer
        fields = ('Name','Phone','Address','Email')
        labels = {
            'Name':'name',
            'Phone':'FRE. Phone'
        }

    def __init__(self, *args, **kwargs):
        super(FreelancerForm,self).__init__(*args, **kwargs)
        self.fields['Address'].empty_label = "Select"
        self.fields['Phone'].required = False

