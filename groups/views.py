from django.shortcuts import get_object_or_404
from rest_framework import generics, status, serializers, permissions
from rest_framework.exceptions import MethodNotAllowed, NotFound
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .models import Group, GroupMembership
from .permissions import IsOwnerOrReadOnly
from .serializers import GroupSerializer, GroupMembershipSerializer


class GroupListCreateView(generics.ListCreateAPIView):
    """
    List all groups, or create a new group.
    Searchable fileds: name, location, description
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'location', 'description']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a group instance.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class GroupMembershipListCreateView(generics.ListCreateAPIView):
    """
    List all group memberships, or create a new group membership.
    """
    serializer_class = GroupMembershipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        group_id = self.kwargs['pk']
        return GroupMembership.objects.filter(group_id=group_id)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        elif not queryset.exists():
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response([])

    def perform_create(self, serializer):
        group_id = self.kwargs['pk']
        user = self.request.user
        group = get_object_or_404(Group, pk=group_id)

        # Check if the user is already a member of the group
        if group.members.filter(user=user).exists():
            raise serializers.ValidationError("User is already a member of this group.")

        serializer.save(user=user, group=group)


class GroupMembershipDeleteView(generics.DestroyAPIView):
    """
    Delete a group membership instance.
    """
    queryset = GroupMembership.objects.all()
    serializer_class = GroupMembershipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        group_id = self.kwargs['pk']
        user_id = self.kwargs['member_pk']

        try:
            group_membership = GroupMembership.objects.get(group_id=group_id, user_id=user_id)
        except GroupMembership.DoesNotExist:
            raise NotFound("Group membership not found")
        
        if request.user == group_membership.user or request.user == group_membership.group.owner:
            group_membership.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_403_FORBIDDEN)
