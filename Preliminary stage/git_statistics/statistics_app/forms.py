from django import forms


class SearchForm(forms.Form):
    """
    Is used to search a repository.
    """
    login = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'owner\'s login'})
    )
    repository = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'repository'})
    )
