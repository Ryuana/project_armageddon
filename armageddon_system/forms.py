from django import forms


class createformForm(forms.Form):
    FORM_ID = forms.DecimalField()
    FORM_NAME = forms.CharField()
    FEE = forms.DecimalField()
    QR = forms.CharField()
