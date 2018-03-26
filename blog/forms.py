from django import forms
from .models import Comments

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

class NewCommentForm(forms.Form):
    class Meta:
        model = Comments
        fields = ('descrption')