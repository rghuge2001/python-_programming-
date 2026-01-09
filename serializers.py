
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Student


# ✅ FOR ADD / UPDATE STUDENT
class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = [
            'id',
            'roll_no',
            'name',
            'email',
            'phone',
            'address',
            'photo',
            'password'
        ]

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data['password']
        )
        return super().create(validated_data)


# ✅ FOR LOGIN ONLY (NO EMAIL)
class StudentLoginSerializer(serializers.Serializer):
    roll_no = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

