from django import forms
h=[('python',"PYTHON"),('django',"DJANGO"),('SQL',"SQL")]
g=[('male',"MALE"),('Female',"FEMALE")]
class SignupForm(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #cours=forms.MultipleChoiceField(choices=h)
    cours=forms.MultipleChoiceField(choices=h,widget=forms.RadioSelect)