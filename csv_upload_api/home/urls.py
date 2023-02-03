from django.urls import path
from home.views import UploadFileView
urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file')
]