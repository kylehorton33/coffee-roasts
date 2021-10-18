from django.forms import ModelForm, TextInput
from .models import Roast

class NewRoastModelForm(ModelForm):
    class Meta:
        model = Roast
        fields = ['roaster', 'bean', 'green_quantity', 'roasted_on', 'time_to_first_crack', 'time_to_cooling', 'roast_quantity', 'roast_level']
        help_texts = {
            'roasted_on': ('<span id="help_start">Click \'START\' to begin roast<span>'),
            'time_to_first_crack': ('<span id="help_crack">Click \'1st CRACK\'<span>'),
            'time_to_cooling': ('<span id="help_cool">Click \'COOL\'<span>'),
        }
        widgets = {
         'roast_level': TextInput(attrs={
             'type': 'range',
             'min': 0,
             'max': 10,
            })
         }
