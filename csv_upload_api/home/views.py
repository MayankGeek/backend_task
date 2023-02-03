from django.shortcuts import render
# Create your views here.
from rest_framework import generics
import io
import csv
import pandas as pd
from rest_framework.response import Response
from home.models import CsvFile
from home.serializers import CsvFileUploadSerializer,SaveFileSerializer

class UploadFileView(generics.CreateAPIView):
    serializer_class = CsvFileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = CsvFile(
                id=row['id'],
                year=row["year"],
                industry_aggregation_NZSIOC=row["Industry_aggregation_NZSIOC"],
                industry_code_NZSIOC=row["Industry_code_NZSIOC"],
                industry_name_NZSIOC=row["Industry_name_NZSIOC"],
                units=row["units"]
            )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
