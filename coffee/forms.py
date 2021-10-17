from django.forms import ModelForm, TextInput
from .models import Roast

class NewRoastModelForm(ModelForm):
    class Meta:
        model = Roast
        fields = ['roaster', 'bean', 'green_quantity', 'roasted_on', 'time_to_first_crack', 'time_to_cooling', 'roast_quantity', 'roast_level']
        help_texts = {
            'roasted_on': ('Click \'START\' to begin roast'),
            'time_to_first_crack': ('Click \'1st CRACK\''),
            'time_to_cooling': ('Click \'COOL\''),
        }
        widgets = {
         'roast_level': TextInput(attrs={
             'type': 'range',
             'min': 0,
             'max': 10,
            })
         }
