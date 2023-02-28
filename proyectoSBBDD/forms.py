from django import forms

opcionesFormReporte =(
    ("1", "Falta de agua"),
    ("2", "Contaminacion de agua"),
    ("3", "Poca cantidad de agua"),
)


class formulario_reporte(forms.Form):
    num_usuario = forms.IntegerField()
    movtivo_reporte = forms.ChoiceField(choices= opcionesFormReporte)
    