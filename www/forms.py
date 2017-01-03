from django import forms

class ContactMe(forms.Form):
    message = forms.CharField(required=True, label="Message:", widget=forms.Textarea)
    name = forms.CharField(requeried=True, label="Name:" max_length: 30)
    email = forms.EmailField(required=True, label="Email:")

"""
<form role="form" action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

Reference: https://hellowebapp.com/news/tutorial-setting-up-a-contact-form-with-django/
"""
