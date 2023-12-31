from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from groups.models import BaseModel
from django_resized import ResizedImageField


class Event(BaseModel):
    """
    Defines an Event model.
    Inherits from BaseModel.

    attributes:
        organizer (User): Reference to User. The organizer of the event.
        name (str): The name of the event.
        date (date): The date of the event.
        time (time): The time of the event.
        difficulty (str): The difficulty of the event.
        image (ImageField): The image of the event.
    """
    DIFFICULTY_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]
    owner = models.ForeignKey(get_user_model(), related_name="organized_events", on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    date = models.DateField(default=datetime.now() + timedelta(weeks=1))
    time = models.TimeField(default=datetime.strptime("08:00:00", "%H:%M:%S").time())
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES, default="beginner")
    image = ResizedImageField(
        size=[768, 1024],
        default="events/images/default.png",
        upload_to="events/images",
    )

    class Meta:
        db_table = "events"
        ordering = ["-created_at"]

    def __str__(self):
        """
        Return a string representation of the `Event`
        """
        return self.name

@receiver(post_save, sender=Event)
def create_event_attendance(sender, instance, created, **kwargs):
    if created:
        EventAttendance.objects.create(event=instance, user=instance.owner, is_admin=True)


class EventAttendance(models.Model):
    """
    Define an EventAttendance model.

    attributes:
        user (User): Reference to User.
        event (Event): Reference to Event.
        is_admin (bool): Whether the user is an admin of the event.
        joined_at (datetime): The date and time a user joined an event.
    """
    user = models.ForeignKey(get_user_model(), related_name="events",  on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="attendees", on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = "event_attendance"
        unique_together = ["user", "event"]
        ordering = ["-joined_at"]

    def __str__(self):
        """
        Return a string representation of the `EventAttendance`
        """
        return f"{self.user.username} is attending {self.event.name}"
