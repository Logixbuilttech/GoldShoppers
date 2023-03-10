from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def Users_list(request):
    if request.method == 'GET':
        students = Users.objects.all()
        serializers = UsersSerializers(students,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        serializers = UsersSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def Company_Information_list(request):
    if request.method == 'GET':
        students = Company_Information.objects.all()
        serializers = Company_InformationSerializers(students,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        serializers = Company_InformationSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Vendors_list(request):
    if request.method == 'GET':
        students = Vendors.objects.all()
        serializers = VendorsSerializers(students,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        serializers = VendorsSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def Users_details(request,pk):
    try:
        users = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = UsersSerializers(Users)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = UsersSerializers(Users,data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def Company_Information_details(request,pk):
    try:
        users = Company_Information.objects.get(pk=pk)
    except Company_Information.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = Company_InformationSerializers(Company_Information)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = Company_InformationSerializers(users,data= request.data)
        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def Vendors_details(request,pk):
    try:
        users = Vendors.objects.get(pk=pk)
    except Vendors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = VendorsSerializers(Vendors)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = VendorsSerializers(users,data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

































































# from django.shortcuts import render,redirect
# from . models import *
# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect
# # Create your views here.

# def index(request): 
#     jobs = Users.objects.all()
    
#     return render(request, "index.html",{'jobs':jobs})

# def admin_dashboard(request): 
#     if request.user.is_authenticated:
#         users = Users.objects.all()
#         # if request.method == "POST":         
#         #     w = Jobseeker.objects.get(id=request.POST['id'])
#         #     w.is_active = request.POST['is_active'] == 'True'
#         #     w.save()
#         #     return redirect('admin_dashboard')


#         return render(request, "index.html",{'user':users})
#     alert = True
#     return render(request, "index.html", {'alert':alert})

# def delete_user(reqeest,myid):
#     user = Users.objects.filter(id = myid)
#     user.delete()
    
#     return HttpResponseRedirect("/")

# def admin_side_EditUser(request, myid):
#     user = Users.objects.filter(id=myid).first()
#     if request.method == "POST":
#         username=request.POST.get('username')
#         first_name=request.POST.get('first_name')
#         last_name=request.POST.get('last_name')
#         phone_number = request.POST.get('phone_number')
#         email = request.POST.get('email')
#         is_staff = request.POST.get('is_staff') 
#         is_active = request.POST.get('is_active') 
#         try:
#             print()
#             u = Users.objects.get(id=user.id)          
#             u.username = username
#             u.first_name = first_name
#             u.last_name = last_name
#             u.phone_number = phone_number
#             u.email = email
#             u.is_staff = is_staff
#             u.is_active = is_active
#             u.save()
#             print("+++++++++++++++++++++++++++++++++++++++++++",u.last_name)
#             # return render(request, "admin_side_AddJob.html")
#             return redirect('admin_dashboard')
#         except:
#             pass
#     return render(request, "admin_side_EditUser.html",{'user':user})

# def Logout(request):
#     logout(request)
#     # messages.success(request,"you logged out")
#     return HttpResponseRedirect("/")