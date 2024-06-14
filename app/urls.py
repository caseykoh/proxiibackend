from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import InquirySubmissionView, AvailabilityView

app_router = DefaultRouter()

app_router.register(r'inquiry-submission', InquirySubmissionView)
app_router.register(r'availability', AvailabilityView)

urlpatterns = [
    path('', include(app_router.urls)),
]