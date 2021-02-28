from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import PersonalInfo
from api.serializers.UserPersonalInfoSerializer import PersonalInfoSerializer


class CreateAndListPersonalInfoRecordView(ListCreateAPIView):
    """
    This endpoint can only be used to CREATE new records in the "PersonalInfo" model and to list all the stored records
    in the same table.
    Note: This endpoint shall be only accessible to the authenticated users.
    """
    serializer_class = PersonalInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PersonalInfo.objects.all()

    def perform_create(self, serializer):
        # As all other field values than user_account is processed through the serializer. We store the user
        # field value manually from the request.
        serializer.save(user=self.request.user)


class FetchUpdateDeletePersonalInfoRecordView(RetrieveUpdateDestroyAPIView):
    """
    This endpoint is used to Fetch, Update and Delete any record from the "PersonalInfo" model
    Note: This endpoint shall be only accessible to the authenticated users.
    """
    serializer_class = PersonalInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return PersonalInfo.objects.filter(user=self.request.user)
