from django import forms
from fluent_comments.forms import FluentCommentForm
from django.utils.translation import ugettext_lazy


class CommentForm(FluentCommentForm):
    email = forms.EmailField(label=ugettext_lazy("Email address"),
                             required=False)
