from django import forms
from django.core import validators

# def name_start_with(value):
#     if value[0].lower()!='h':
#         raise forms.ValidationError('Name should start with h')
    

# def valid_email(mail):
#         if mail[-10::]!='@gmail.com':
#             raise forms.ValidationError('invalid email')



            


class Registration(forms.Form):
    name=forms.CharField(max_length=20,label='Name')  #,validators=[name_start_with]

    age=forms.IntegerField(label='Age')
    marks=forms.IntegerField(label='Marks')
    email=forms.EmailField(widget=forms.EmailInput)  #,validators=[valid_email]
    pwd=forms.CharField(label='password',widget=forms.PasswordInput)
    rpwd=forms.CharField(label='confirm password',widget=forms.PasswordInput)
    feedback=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'placeholder':'Please give Feedback'}))
    bot_data=forms.CharField(max_length=20,required=False,widget=forms.HiddenInput)


    def clean(self):
        data=super().clean()
        age=data['age']
        if age<18:
            raise forms.ValidationError('Age should be greater than 18')
        
        password=data['pwd']
        cpassword=data['rpwd']
        if password!=cpassword:
            raise forms.ValidationError('Re Enter password not matched')
        
        bot=data['bot_data']
        if len(bot)>=0:
            raise forms.ValidationError("Form filed by bot so i will not accept")

    def clean_name(self):
        nval=self.cleaned_data['name']
        if len(nval)<4:
            raise forms.ValidationError('Length of name should be greater then 4 charector')
        return nval
        

    # def clean_email(self):
    #     mail=self.cleaned_data['email']
    #     if mail[-10::]!='@gmail.com':
    #         raise forms.ValidationError('invalid email id')
    #     return mail
        

    # def clean_age(self):
    #     age=self.cleaned_data['age']
    #     if age<18 or age>60:
    #         raise forms.ValidationError('enter age more than 10 year and less than 60')
    #     return age