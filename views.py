from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password

from .models import Student
from .serializers import StudentSerializer


# ================= STUDENT LIST & CREATE =================
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ================= STUDENT DETAIL =================
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        student.delete()
        return Response(
            {"message": "Student deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )


# ================= STUDENT LOGIN =================
@api_view(['POST'])
def student_login(request):
    roll_no = request.data.get('roll_no')
    password = request.data.get('password')

    if not roll_no or not password:
        return Response(
            {"error": "Roll number आणि password आवश्यक आहे"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        student = Student.objects.get(roll_no=roll_no)
    except Student.DoesNotExist:
        return Response(
            {"error": "Roll number किंवा password चुकीचा आहे"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not check_password(password, student.password):
        return Response(
            {"error": "Roll number किंवा password चुकीचा आहे"},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(
        {
            "message": "Login successful",
            "student_id": student.id,
            "name": student.name
        },
        status=status.HTTP_200_OK
    )
