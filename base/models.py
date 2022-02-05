from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Classes represent DB tables
# Every attribute in the class reps a col in the DB
# Every instance of the class reps a row in the DB


class Topic(models.Model):
    """
    Model which represents a topic.
    Relation with Room: One-to-many
    """
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)

class Room(models.Model):
    """
    Model which represents the Room in the DB
    Relation with Messages: One-to-many
    """
    # User that hosts the room
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # When a topic is deleted, do not delete the room and allow the topic to be empty
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # null=True: can be blank so db can have an instance with a blank description
    # blank=True: When save method/submit form, it can be empty
    description = models.TextField(null=True, blank=True) # Same thing as a CharField just bigger
    # participants =
    # auto_now: Any time save is run to update model, save a timestamp
    updated = models.DateTimeField(auto_now=True)
    # auto_now_add=True: Only take a timestamp when we first create the instance
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

class Message(models.Model):
    """
    Model which represents user messages in a room
    Relation with Room: One-to-many
    Relation with User: One-to-many
    A single room can have many messages.
    A single user can also have many messages.
    """
    # When a user is deleted, delete all their messages
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Est relationship to the Room
    # When a room gets deleted, all the Messages will get deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        # Trim down for a preview
        return self.body[0:50]
