from django import forms
from blog_app.models import Comment

class EmailSending_form(forms.Form):
    name = forms.CharField()
    From_Mail = forms.EmailField()
    To_Mail = forms.EmailField()
    Comment = forms.CharField(required= False,widget = forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('Name','Email','Body_comment')
