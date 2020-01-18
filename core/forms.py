from django import forms

class ContactUsForm(forms.Form):
    name22 = forms.CharField(label='name', max_length=10)
    message22 = forms.CharField(label='message', widget=forms.Textarea)
    status22 = forms.ChoiceField(label='age', choices=((1, "Not relevant"),
                                        (2, "Review"),
                                        (3, "Maybe relevant"),
                                        (4, "Relevant"),
                                        (5, "Leading candidate")))

    def clean(self):
        #https://docs.djangoproject.com/en/3.0/ref/forms/validation/#using-validation-in-practice
        cleaned_data = super().clean()
        user_name = cleaned_data.get("name22")
        print(f'user_name form cleaned_data {user_name}')

        if len(user_name) < 2:
            msg=" Too short name"
            self.add_error("name22", msg)