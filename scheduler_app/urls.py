from django.urls import path
from .views import register, verify_email, request_otp, verify_otp, delete_meeting

urlpatterns = [
    path('register/', register, name='register'),
    path('verify/', verify_email, name='verify'),
    path('request-otp/', request_otp, name='request_otp'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('delete_meeting/', delete_meeting, name='soft_delete_meeting'),

]