from django import forms
from django.contrib.auth.models import User
from artapp.models import artwork1,more,more2,details

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('first_name','last_name','username','password','email')
        
class useredit(forms.ModelForm):
    class Meta():        
        model=User
        fields=('first_name','last_name','username',)
        
class artworkform1(forms.ModelForm):
    class Meta():
        model=artwork1
        fields=('art',) 

        
class moreform(forms.ModelForm):
    class Meta():
        model=more
        fields=('ppic',)
        
class moreform2(forms.ModelForm):
    class Meta():
        model=more2
        fields=('coverphoto',)
        
class detailsform(forms.ModelForm):
    class Meta():
        model=details
        fields=('age','Dob','about','link','link1',)
        
