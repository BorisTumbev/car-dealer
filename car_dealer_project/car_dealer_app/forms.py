from django.forms import ModelForm
from .models import RentalVehicle, Make, Model, SellVehicle,MyUser,Message
from django import forms
from .widgets import RelatedFieldWidgetCanAdd, DateTimeInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    """
    form for user creation
    """
    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
       
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('first_name','last_name','username','email','image','role')

class CustomUserChangeForm(UserChangeForm):
    """
    form for user change
    """
   
    def __init__(self, *args, **kwargs):

        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        for fieldname in ['username','password']:
            self.fields[fieldname].help_text = None
            
        if not user.is_superuser:
            del self.fields['role']
            del self.fields['username']
        

    def clean_password(self):
        return self.clean_password

    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ('first_name','last_name','username','email','image','role')
        


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
        exclude = ('rented_at','created_at','user','rental_status','rented_until')

class RentForm(MyForm):

    """
    form for rental vehicle model
    """
    make = None
    model = None

    class Meta:
        model  = RentalVehicle
        fields = ['rented_until']
        widgets = {
            'rented_until':DateTimeInput(),
        }

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

    class Meta:
        model  = Model
        fields = '__all__'


class MessageForm(MyForm):
    """
    form for messages
    """
    make = None
    model = None

    class Meta:
        model  = Message
        fields = ['description']
       