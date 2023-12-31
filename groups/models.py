from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField


class BaseModel(models.Model):
    """
    Defines all common fields in Group and Event models.

    attributes:
        description (str): The description of a group or event.
        location (str): The location of a group or event.
        created_at (datetime): The date and time a group or event was created.
        updated_at (datetime): The date and time a group or event was last updated.
    """
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Group(BaseModel):
    """
    Define a Group model.
    Inherits from BaseModel.

    attributes:
        owner (User): Reference to User. The owner of the group.
        name (str): The name of the group. Must be unique.
        image (ImageField): The image of the group.
    """
    owner = models.ForeignKey(get_user_model(), related_name="owned_groups", on_delete=models.CASCADE)
    name = models.CharField(max_length=225, unique=True)
    image = ResizedImageField(
        size=[768, 1024],
        default="groups/images/default.png",
        upload_to="groups/images",
    )


    class Meta:
        db_table = "groups"
        ordering = ["-created_at"]


    def __str__(self):
        """
        Return a string representation of the `Group`
        """
        return self.name


@receiver(post_save, sender=Group)
def create_group_membership(sender, instance, created, **kwargs):
    if created:
        GroupMembership.objects.create(group=instance, user=instance.owner, is_admin=True)


class GroupMembership(models.Model):
    """
    Define a GroupMembership model.

    attributes:
        user (User): Reference to User.
        group (Group): Reference to Group.
        is_admin (bool): Whether the user is an admin of the group.
        joined_at (datetime): The date and time the user joined the group.
    """
    user = models.ForeignKey(get_user_model(), related_name="member_groups", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="members", on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "group_memberships"
        unique_together = ["user", "group"]
        ordering = ["-joined_at"]

    def __str__(self):
        """
        Return a string representation of the `GroupMembership`
        """
        return f"{self.user.username} is a member of {self.group.name}"

