from django import forms


class Input_financedata_info(forms.Form):

    start = forms.DecimalField(max_digits=22, decimal_places=16)
    end = forms.DecimalField(max_digits=22, decimal_places=16)