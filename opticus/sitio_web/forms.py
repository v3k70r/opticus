from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    asunto = forms.CharField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)