from django import forms


class ContactForm(forms.Form):
    Motivo = forms.CharField(max_length=255)
    mensagem = forms.CharField(widget=forms.Textarea)
