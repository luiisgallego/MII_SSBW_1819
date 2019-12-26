from .models import Pelis
from mongodbforms import DocumentForm
from mongodbforms import EmbeddedDocumentForm
from django.forms import TextInput, Textarea, NumberInput
from django.utils.translation import gettext_lazy as _

class PelisForm(DocumentForm):
	class Meta:
		model = Pelis
		fields = [ "title", "year", "director"]
		widgets = {
            "title": TextInput(attrs={ "class":"form-control" }),
            "year": NumberInput(attrs={ "class":"form-control" }),
            "director": TextInput(attrs={ "class":"form-control" }),
        }	

		
