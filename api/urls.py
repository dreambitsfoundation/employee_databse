from django.urls import path

from api.views.PersonalInfoView import CreateAndListPersonalInfoRecordView, FetchUpdateDeletePersonalInfoRecordView
from api.views.ProfessionalInfoView import FetchUpdateDeleteProfessionalInfoRecordView, \
    CreateAndListProfessionalInfoRecordView
from api.views.UserAccountView import UserAccountView
from api.views.UserLoginView import UserLoginView

urlpatterns = [
    path('user_account/', UserAccountView.as_view(), name='user_account'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('personal_info/<int:id>', FetchUpdateDeletePersonalInfoRecordView.as_view(),
         name="fetch_update_delete_personal_info"),
    path('personal_info/', CreateAndListPersonalInfoRecordView.as_view(), name='create_list_personal_info'),
    path('professional_info/<int:id>', FetchUpdateDeleteProfessionalInfoRecordView.as_view(),
         name="fetch_update_delete_professional_info"),
    path('professional_info/', CreateAndListProfessionalInfoRecordView.as_view(), name='create_list_professional_info'),
]
