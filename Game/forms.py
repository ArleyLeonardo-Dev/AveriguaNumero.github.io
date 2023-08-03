from django import forms 

class Game(forms.Form):
	numero = forms.IntegerField(label = "NUMERO")