from django import forms

# our new form
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    comment = forms.CharField(
        required=True,
        widget=forms.Textarea
    )