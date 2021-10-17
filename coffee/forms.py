from django.forms import ModelForm
from .models import Roast

class NewRoastModelForm(ModelForm):
    class Meta:
        model = Roast
        exclude = ('roast_log',)
        help_texts = {
            'roasted_on': ('Date of roast in UTC.'),
        }
