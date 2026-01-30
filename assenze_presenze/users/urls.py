from django.urls import path
from .views import (
    ParticipantProfileView,
    CurrentUserView,
    RegisterView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("participant/profile/", ParticipantProfileView.as_view(), name="participant-profile"),
    path("me/", CurrentUserView.as_view(), name="current-user"),
]
