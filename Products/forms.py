from django import forms


class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
