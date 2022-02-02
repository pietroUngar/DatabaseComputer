from django import forms
from .models import *


class ComputerForm(forms.ModelForm):

    class Meta:

        model = Computer
        fields = (

            "position", "broken",
            "MAC_number", "processor_type", "core_number",
            "ram_dimension", "disk_dimension", "video_card"

        )
