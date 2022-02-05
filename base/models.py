from statistics import mode
from django.db import models

# Create your models here.
# Classes represent DB tables
# Every attribute in the class reps a col in the DB
# Every instance of the class reps a row in the DB

class Room(models.Model):
    """
    Model which represents the Room in the DB
    """
    # host =
    # topic = 
    name = models.CharField(max_length=200)
    # null=True: can be blank so db can have an instance with a blank description
    # blank=True: When save method/submit form, it can be empty
    description = models.TextField(null=True, blank=True) # Same thing as a CharField just bigger
    # participants =
    # auto_now: Any time save is run to update model, save a timestamp
    updated = models.DateTimeField(auto_now=True)
    # auto_now_add=True: Only take a timestamp when we first create the instance
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return str representation of the model
        """
        self.name
