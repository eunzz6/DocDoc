from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    file = forms.FileField(required=False)
    file2 = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': '.csv'}),required=False)