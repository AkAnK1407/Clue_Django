# from django.forms import ModelForm, fields
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Student
# from django.contrib.auth.forms import AuthenticationForm

# class CustomUserRegister( UserCreationForm):
#     username =forms.CharField(widget =forms. TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
#     email = forms.CharField(widget =forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'abc@banasthali.in'}))
#     password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
#     password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']
        


# class StudentSignupForm(forms.ModelForm):
#     confirm_password = forms.CharField(
#         label="Confirm Password",
#         widget=forms.PasswordInput,
#         required=True
#     )

#     class Meta:
#         model = Student
#         fields = ["email", "username", "password"]  # Match model fields
#         widgets = {
#             "password": forms.PasswordInput(),
#         }

#     def clean_email(self):
#         """ Validate that the email ends with @banasthali.in """
#         email = self.cleaned_data.get("email")
#         if not email.endswith("@banasthali.in"):
#             raise forms.ValidationError("Email must be from @banasthali.in domain.")
#         return email

#     def clean(self):
#         """ Validate that password and confirm password match """
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError({"confirm_password": "Passwords do not match."})

#         return cleaned_data

#     def save(self, commit=True):
#         """ Save the user after hashing the password """
#         student = super().save(commit=False)
#         student.set_password(self.cleaned_data["password"])  # Hash password
#         if commit:
#             student.save()
#         return student



# class StudentLoginForm(forms.Form):
#     email = forms.EmailField(
#         label="Email ID",
#         max_length=100,
#         widget=forms.EmailInput(attrs={'class': 'form-control'}),
#     )
#     password = forms.CharField(
#         label="Password",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#     )


# class CoordinatorLoginForm(AuthenticationForm):
#     username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
