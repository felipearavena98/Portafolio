from django import forms
from .models import Usuario


class FormularioUsuario(forms.ModelForm):
    correo = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = Usuario
        fields = ('__all__')

    def clean_email(self):
        correo = self.cleaned_data.get("correo")
        if Usuario.objects.filter(correo=correo).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return correo