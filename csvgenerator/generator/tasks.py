# from celery import shared_task
import pandas as pd
import io
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# @shared_task
def generate_csv(columns, num_records):
    data = {}
    for column in columns:
        name = column['name']
        dtype = column['dtype']
        if dtype == 'int':
            data[name] = pd.Series([i for i in range(num_records)], dtype=int)
        elif dtype == 'float':
            data[name] = pd.Series([float(i) for i in range(num_records)], dtype=float)
        elif dtype == 'str':
            data[name] = pd.Series([f'str_{i}' for i in range(num_records)], dtype=str)

    df = pd.DataFrame(data)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_content = csv_buffer.getvalue()

    file_name = 'generated_data.csv'
    file_path = default_storage.save(file_name, ContentFile(csv_content))

    return file_path
