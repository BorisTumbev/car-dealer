from django.forms import ModelForm
from .models import Vehicle, Make, Model
from django import forms

class MyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        return super().save(*args, **kwargs)



class VehicleForm(MyForm):


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



# class SellForm(forms.Form):
#     field1 = forms.IntegerField(label="first field")
    
