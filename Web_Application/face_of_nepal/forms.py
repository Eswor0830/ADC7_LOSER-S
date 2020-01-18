from django import forms
from face_of_nepal.models import Freelancer
#DataFlair
class FreelancerCreate(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = '__all__'