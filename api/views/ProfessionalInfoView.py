from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import ProfessionalInfo
from api.serializers.UserProfessionalInfoSerializer import ProfessionalInfoSerializer


class CreateAndListProfessionalInfoRecordView(ListCreateAPIView):
    """
    This endpoint shall be used to create and list records from the ProfessionalInfo model.
    Note: This endpoint is only accessible by authenticated user.
    """
    serializer_class = ProfessionalInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProfessionalInfo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FetchUpdateDeleteProfessionalInfoRecordView(RetrieveUpdateDestroyAPIView):
    """
    This endpoint is used to Fetch, Update and Delete any record from the "ProfessionalInfo" table
    Note: This endpoint is only accessible by authenticated user.
    """
    serializer_class = ProfessionalInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return ProfessionalInfo.objects.filter(user=self.request.user)
