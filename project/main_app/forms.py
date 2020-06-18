from django import forms


class ManagerForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': "Имя",
                                                                            'name': "first_name",
                                                                            }))
    phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': "Телефон",
                                                                            'name': "phone",
                                                                            }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': "Email",
                                                                          'name': "email",
                                                                          }))


class ContactForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': "Имя",
                                                                            'name': "first_name",
                                                                            }))
    phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': "Телефон",
                                                                            'name': "phone",
                                                                            }))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': "Email",
                                                                           'name': "email",
                                                                           }))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                           'placeholder': "Сообщение",
                                                                           'name': "message",
                                                                           }))

