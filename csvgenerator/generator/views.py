from rest_framework import status, views
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import io
from .serializers import GenerateRequestSerializer

def index(request):
    return render(request, 'generator/index.html')

class GenerateCSVView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = GenerateRequestSerializer(data=request.data)
        if serializer.is_valid():
            columns = serializer.validated_data['columns']
            num_records = serializer.validated_data['num_records']

            # Generate CSV content
            data = {}
            for column in columns:
                name = column['name']
                dtype = column['dtype']
                if dtype == 'int':
                    data[name] = [i for i in range(num_records)]
                elif dtype == 'float':
                    data[name] = [float(i) for i in range(num_records)]
                elif dtype == 'str':
                    data[name] = [f'str_{i}' for i in range(num_records)]

            df = pd.DataFrame(data)
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            csv_content = csv_buffer.getvalue()

            # Create HTTP response with CSV file
            response = HttpResponse(csv_content, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="generated_data.csv"'
            return response

        print("Validation Errors:", serializer.errors)  # For debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
