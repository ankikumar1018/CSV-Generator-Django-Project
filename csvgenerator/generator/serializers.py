from rest_framework import serializers

class ColumnSerializer(serializers.Serializer):
    name = serializers.CharField()
    dtype = serializers.ChoiceField(choices=[('int', 'Integer'), ('float', 'Float'), ('str', 'String')])

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Column name cannot be empty.")
        return value

class GenerateRequestSerializer(serializers.Serializer):
    columns = ColumnSerializer(many=True)
    num_records = serializers.IntegerField()

    def validate_num_records(self, value):
        if value <= 0:
            raise serializers.ValidationError("Number of records must be a positive integer.")
        return value
