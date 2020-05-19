from django import forms
class ProductInsertForm(forms.Form):
    pid=forms.IntegerField(
        label="ID:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-class',
                'placeholder':'Enter ID'
            }
        )
    )
    pname=forms.CharField(
        label="Product Name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-class',
                'placeholder':'Prod Name'
            }
        )
    )
    pcost=forms.IntegerField(
        label="Product Cost:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-class',
                'placeholder':'Prod Cost'
            }
        )
    )
    pcolor=forms.CharField(
        label='Product Color:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'prod color'
            }
        )
    )
    pclass=forms.CharField(
        label="Product Class:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'prod class'
            }
        )
    )
    cname=forms.CharField(
        label="Customer Name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'custom name'
            }
        )
    )
    cmobile=forms.IntegerField(
        label="Customer Mobile:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Cust Mob'
            }
        )
    )
    cemail=forms.EmailField(
        label="Customer Email:",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Cust Email'
            }
        )
    )
class ProductUpdateForm(forms.Form):
    pid = forms.IntegerField(
        label="ID:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-class',
                'placeholder': 'Enter ID'
            }
        )
    )
    pcost = forms.IntegerField(
        label="Product Cost:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-class',
                'placeholder': 'Prod Cost'
            }
        )
    )
class ProductDeleteForm(forms.Form):
    pid = forms.IntegerField(
        label="ID:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-class',
                'placeholder': 'Enter ID'
            }
        )
    )