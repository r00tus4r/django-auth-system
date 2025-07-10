from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['username'].label = 'Username'
        self.fields['username'].label_suffix = ' *'
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        self.fields['username'].error_messages = {
            'required': 'Username is required.',
            'max_length': 'Username must be 150 characters or fewer.',
            'invalid': 'Enter a valid username.'
        }
        self.fields['username'].required = True

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].label_suffix = ' *'
        self.fields['password1'].help_text = 'Required. 8 characters or more.'
        self.fields['password1'].error_messages = {
            'required': 'Password is required.',
            'min_length': 'Password must be at least 8 characters long.',
            'invalid': 'Enter a valid password.'
        }
        self.fields['password1'].required = True

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].label_suffix = ' *'
        self.fields['password2'].help_text = 'Enter the same password as above, for verification.'
        self.fields['password2'].error_messages = {
            'required': 'Password confirmation is required.',
            'invalid': 'Enter a valid password confirmation.'
        }
        self.fields['password2'].required = True

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                mark_safe('This username is already taken. Please choose a different one.'))
        return username

    def as_div(self):
        output = ""
        for field in self:
            output += f'''
            <div class="mb-3 form-group">
                {field.label_tag(attrs={"class": "form-label"})}
                {field}
                {''.join([f'<div class="text-danger small">{error}</div>' for error in field.errors])}
                {f'<div class="text-muted"><small>{field.help_text}</small></div>' if field.help_text else ''}
            </div>
            '''
        return mark_safe(output)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'password' in self.fields:
            del self.fields['password']

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['username'].label = 'Username'
        self.fields['username'].label_suffix = ' *'
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        self.fields['username'].error_messages = {
            'required': 'Username is required.',
            'max_length': 'Username must be 150 characters or fewer.',
            'invalid': 'Enter a valid username.'
        }
        self.fields['username'].required = True

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
        self.fields['email'].label = 'Email Address'
        self.fields['email'].label_suffix = ' *'
        self.fields['email'].help_text = 'Required. Enter a valid email address.'
        self.fields['email'].error_messages = {
            'required': 'Email address is required.',
            'invalid': 'Enter a valid email address.'
        }
        self.fields['email'].required = True

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['first_name'].label = 'First Name'
        self.fields['first_name'].label_suffix = ' *'
        self.fields['first_name'].help_text = 'Optional. Enter your first name.'
        self.fields['first_name'].error_messages = {
            'invalid': 'Enter a valid first name.'
        }
        self.fields['first_name'].required = False

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['last_name'].label_suffix = ' *'
        self.fields['last_name'].help_text = 'Optional. Enter your last name.'
        self.fields['last_name'].error_messages = {
            'invalid': 'Enter a valid last name.'
        }
        self.fields['last_name'].required = False

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                mark_safe('This username is already taken. Please choose a different one.'))
        return username
    
    def as_div(self):
        output = ""
        for field in self:
            output += f'''
            <div class="mb-3 form-group">
                {field.label_tag(attrs={"class": "form-label"})}
                {field}
                {''.join([f'<div class="text-danger small">{error}</div>' for error in field.errors])}
                {f'<div class="text-muted"><small>{field.help_text}</small></div>' if field.help_text else ''}
            </div>
            '''
        return mark_safe(output)

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['username'].label = 'Username'
        self.fields['username'].label_suffix = ' *'
        self.fields['username'].help_text = 'Required. Enter your username.'
        self.fields['username'].error_messages = {
            'required': 'Username is required.',
            'invalid': 'Enter a valid username.'
        }
        self.fields['username'].required = True

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password'].label = 'Password'
        self.fields['password'].label_suffix = ' *'
        self.fields['password'].help_text = 'Required. Enter your password.'
        self.fields['password'].error_messages = {
            'required': 'Password is required.',
            'invalid': 'Enter a valid password.'
        }
        self.fields['password'].required = True

    def as_div(self):
        output = ""
        for field in self:
            output += f'''
            <div class="mb-3 form-group">
                {field.label_tag(attrs={"class": "form-label"})}
                {field}
                {''.join([f'<div class="text-danger small">{error}</div>' for error in field.errors])}
                {f'<div class="text-muted"><small>{field.help_text}</small></div>' if field.help_text else ''}
            </div>
            '''
        return mark_safe(output)