from django import forms
from .models import applicant

class AppplicantForm(forms.ModelForm):
    class Meta:
        model = applicant
        fields = ['name','school', 'photo', 'games','email']
        widgets = {
            'games': forms.CheckboxSelectMultiple(),
        }

    def clean_games(self):
        selected_games = self.cleaned_data['games']
        if selected_games.count() > 2:
            raise forms.ValidationError('You can only select up to two games.')
        return selected_games
class accrej(forms.ModelForm):
    class Meta:
        model = applicant
        fields=['accepted']