from django.forms import ModelForm, Textarea

from consulting.models import Comment, Contact, StudentComment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message')
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 8}),
        }


class StudentCommentForm(ModelForm):
    class Meta:
        model = StudentComment
        fields = ('name', 'message')
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
