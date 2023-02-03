from rest_framework import serializers
from home.models import CsvFile

class CsvFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = CsvFile
        fields = "__all__"