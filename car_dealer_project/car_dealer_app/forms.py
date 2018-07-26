from django.forms import ModelForm
from .models import Vehicle, Make, Model
from django import forms
from .widgets import RelatedFieldWidgetCanAdd

class MyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        return super().save(*args, **kwargs)



class VehicleForm(MyForm):
    make = forms.ModelChoiceField(
       required=True,
       queryset=Make.objects.all(),
       widget=RelatedFieldWidgetCanAdd(Make, related_url="create_make")
                                )
    model = forms.ModelChoiceField(
       required=True,
       queryset=Model.objects.all(),
       widget=RelatedFieldWidgetCanAdd(Make, related_url="create_model")
                                )
    class Meta:
        model  = Vehicle
        exclude = ('sell_status','created_at','user')
       

class MakeForm(MyForm):
    class Meta:
        model  = Make
        fields = '__all__'


class CarModelForm(MyForm):
    class Meta:
        model  = Model
        fields = '__all__'


