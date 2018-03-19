from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

class NewCommentForm(forms.Form):
    new_comment = forms.TextField(help_text="Enter a piece of thoughtful commentary!")

    def clean_comment(self):
        data = self.cleaned_data['renewal_date']

        return data