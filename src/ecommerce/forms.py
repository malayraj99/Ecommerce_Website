from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# Contact Us form


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Full Name"
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Email"
        }
    )

    )
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Your Message"
        }
    ))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # if not "gmail.com" in email:
        #     raise forms.ValidationError("Your Email has to be gmail.com")
        return email

# Login page form


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Username"
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password"
        }
    ))

# Create an account form


class RegisterForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Username"
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Email"
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password"
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password"
        }
    ))

    # Function to prohibit making duplicate usernames

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Will show error message above username box
        qs = User.objects.filter(username=username)
        if qs.exists():  # query set
            raise forms.ValidationError("Username is already taken.")

    # Function tocheck if an account already exists with the email
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Will show error message above email box
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(
                "An account already exists with this email.")

    # Function to check if the passwords match
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError("Passwords must Match")

        return data
