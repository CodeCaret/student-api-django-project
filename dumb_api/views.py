# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from dumb_api.models import StudentDetail
from dumb_api.serializers import StudentDetailSerializer

# import io

@api_view(['GET','POST'])
def students(request):
        
    if request.method == 'GET':
        complex_stu_data = StudentDetail.objects.all()
        serializer = StudentDetailSerializer(complex_stu_data, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        deserializer = StudentDetailSerializer(data = request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data, status=status.HTTP_201_CREATED)
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @csrf_exempt
# def students(request):
        
#     if request.method == 'GET':

#         complex_stu_data = StudentDetail.objects.all()
#         serializer = StudentDetailSerializer(complex_stu_data, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data)
    

#     # if request.method == 'GET':

#     #     complex_stu_data = StudentDetail.objects.get(id = 1)
#     #     print(type(complex_stu_data))

#     #     stu_data = {
#     #         'name':complex_stu_data.name,
#     #         'age':complex_stu_data.age,
#     #         'course':complex_stu_data.course
#     #     }
#     #     print(type(stu_data))
#     #     return JsonResponse(stu_data)




#     elif request.method == 'POST':
#         byte_data = request.body
#         stream_data = io.BytesIO(byte_data)
#         py_data = JSONParser().parse(stream_data)
#         deserializer = StudentDetailSerializer(data = py_data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return JsonResponse({'msg':'Data created successfully!!'}, status = 201)
#         return JsonResponse({'msg':'Something went wrong'}, status = 400)











    # elif request.method == 'POST':
    #     byte_data = request.body
    #     py_data = json.loads(byte_data)
    #     # print(py_data)
    #     StudentDetail.objects.create(
    #             name = py_data['name'],
    #             age = py_data['age'],
    #             course = py_data['course']
    #         )
    #     return JsonResponse({'msg':'Data created successfully!!'}, status = 201)

    # else:
    #     return JsonResponse({'msg':'Method not allowed'}, status = 405)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_update_delete_student(request, pk):

    try:
        student = StudentDetail.objects.get(id = pk)
    except StudentDetail.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentDetailSerializer(student)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        deserializer = StudentDetailSerializer(student, data = request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data, status = status.HTTP_200_OK)
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'PATCH':
        deserializer = StudentDetailSerializer(student, data = request.data, partial = True)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data, status = status.HTTP_200_OK)
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    


# @csrf_exempt
# def get_update_delete_student(request, pk):

#     try:
#         student = StudentDetail.objects.get(id = pk)
#     except StudentDetail.DoesNotExist:
#         return JsonResponse({'msg':f'Student with id {pk} not found'}, status = 404)

#     if request.method == 'GET':
#         serializer = StudentDetailSerializer(student)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         byteData = request.body
#         stream_data = io.BytesIO(byteData)
#         py_data = JSONParser().parse(stream_data)
#         deserializer = StudentDetailSerializer(student, data = py_data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return JsonResponse({'msg':'Data Updated Successfully!!'}, status = 200)
#         return JsonResponse({'msg':'Something went wrong'}, status = 400)
    
    
#     elif request.method == 'PATCH':
#         byteData = request.body
#         stream_data = io.BytesIO(byteData)
#         py_data = JSONParser().parse(stream_data)
#         deserializer = StudentDetailSerializer(student, data = py_data, partial = True)
#         if deserializer.is_valid():
#             deserializer.save()
#             return JsonResponse({'msg':'Data Updated Successfully!!'}, status = 200)
#         return JsonResponse({'msg':'Something went wrong'}, status = 400)

#     elif request.method == 'DELETE':
#         student.delete()
#         return JsonResponse({'msg':'Data Deleted Successfully!!'}, status = 200)

#     else:
#         return JsonResponse({'msg':'Method not allowed'}, status = 405)