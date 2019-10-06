"""Views for docs"""
from django.views import generic

from .models import Doc


class ListView(generic.ListView):
    """Index view"""

    context_object_name = "docs"
    model = Doc
