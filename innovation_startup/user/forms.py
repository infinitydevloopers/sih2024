from django import forms
from .models import User
from .models import Research 
from .models import Innovation


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'confirm_password', 'role', 'phone_no', 'address', 'citizenship']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password do not match")

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

#Reasearch
class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = [
            'research_id', 'title', 'abstract', 'lead_researcher', 
            'status', 'start_date', 'end_date', 
            'related_patent', 'related_publication'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


#Innovation 
class InnovationForm(forms.ModelForm):
    class Meta:
        model = Innovation
        fields = [
            'innovation_id', 'title', 'description', 
            'related_research', 'related_ipr', 'associated_startup', 
            'status'
        ]
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'datetime-local'}),
            'updated_at': forms.DateInput(attrs={'type': 'datetime-local'}),
        }
from django import forms
from .models import Investment

class InvestmentAdminForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial choices for `round` based on `investment_type`
        investment_type = self.data.get('investment_type') or self.instance.investment_type
        if investment_type == 'Startup':
            self.fields['round'].choices = [
                ('Seed', 'Seed'),
                ('Series 1', 'Series 1'),
                ('Series 2', 'Series 2'),
                ('Series 3', 'Series 3'),
                ('IPO', 'IPO')
            ]
        elif investment_type == 'Innovation':
            self.fields['round'].choices = [
                ('Concept', 'Concept'),
                ('Prototype', 'Prototype'),
                ('Development', 'Development'),
                ('Deployed', 'Deployed')
            ]
