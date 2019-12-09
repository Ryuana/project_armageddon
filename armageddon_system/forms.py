from django import forms


# Djangoの入力フォーム生成用の機能

class createformForm(forms.Form):
    FORM_ID = forms.IntegerField()
    FORM_NAME = forms.CharField()
    FEE = forms.IntegerField()
    ISSUANCE_DAYS = forms.IntegerField()
    QR = forms.CharField()
