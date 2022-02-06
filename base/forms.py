from django.forms import ModelForm
from base.models import Room

class RoomForm(ModelForm):
    """Form for creating a Room"""
    class Meta:
        model = Room        # Model that we want to create a room for
        fields = '__all__'  # Create fields based on meta data of Room