from django import forms

class VideoForm(forms.Form):
    url = forms.URLField(label='Youtube Video',max_length=200)