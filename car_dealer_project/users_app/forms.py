from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from .models import MyUser
from django.core.exceptions import ValidationError


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

    def clean_email(self):
        email = self.cleaned_data['email']
        if MyUser.objects.filter(email__iexact=email).exists():
            raise ValidationError("There is user registered with the specified email address!")

        return email

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
        


class CustomPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for fieldname in [ 'old_password', 'new_password1']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = MyUser
        fields = '__all__'


class CustomPasswordResetFrom(PasswordResetForm):
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not MyUser.objects.filter(email__iexact=email).exists():
            raise ValidationError("There is no user registered with the specified email address!")

        return email