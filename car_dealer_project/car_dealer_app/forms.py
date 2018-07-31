from django.forms import ModelForm
from .models import RentalVehicle, Make, Model, SellVehicle
from django import forms
from .widgets import RelatedFieldWidgetCanAdd

class MyForm(ModelForm):
    """
    form for overriding __init__ and save method to get and save user from session
    """
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
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        return super().save(*args, **kwargs)


class RentalVehicleForm(MyForm):

    """
    form for rental vehicle model
    """

    class Meta:
        model  = RentalVehicle
        exclude = ('rented_at','created_at','user','rental_status')

class SellVehicleForm(MyForm):

    """
    form for sell vehicle model
    """
    
    class Meta:
        model  = SellVehicle
        exclude = ('sell_status','created_at','user')



class MakeForm(MyForm):
    """
    form for Make model
    """
    make = None
    model = None
    class Meta:
        model  = Make
        fields = '__all__'


class CarModelForm(MyForm):
    """
    form for Car Model model
    """
    model = None
    # make = forms.ModelChoiceField(
    #    required=True,
    #    queryset=Make.objects.all(),
    #    widget=RelatedFieldWidgetCanAdd(Make, related_url="create_make")
                                # )
    class Meta:
        model  = Model
        fields = '__all__'

