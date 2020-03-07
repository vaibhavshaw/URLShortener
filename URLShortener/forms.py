from django import forms
from .validators import validate_url


class SubmitUrlForm(forms.Form):
    url = forms.CharField(
        max_length=500, label="", validators=[validate_url, ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Long URL",
                "class": "form-control",
            }
        ))
