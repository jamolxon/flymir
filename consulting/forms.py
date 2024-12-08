from django.forms import ModelForm, Textarea
from .models import Comments, Contact

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'phone', 'message')
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 8}),
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'number', 'message',)
        widgets = {
            'message':Textarea(attrs={"autocomplete":"off", 'cols':40, 'rows':10}),
        }
