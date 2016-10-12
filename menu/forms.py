from django import forms
from .models import Menu


def valid_not_empty(data):
    if len(data) < 1:
        raise forms.ValidationError('Must be not be empty')


class MenuForm(forms.ModelForm):
    season = forms.CharField(validators=[valid_not_empty])

    class Meta:
        model = Menu
        fields = ['season', 'items', 'expiration_date']
        exclude = ('created_date',)
