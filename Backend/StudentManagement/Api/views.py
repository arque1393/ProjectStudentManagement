
from django.http import JsonResponse, HttpResponse, HttpRequest
from types import SimpleNamespace
from django.contrib.auth import login as login_user
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Student, Faculty
student = SimpleNamespace()


@api_view(["POST"])
def signup(req):
    username = req.data['username']
    email = req.data['email']
    passwd = req.data['passwd']
    designation = req.data['designation']
    data = {'success': 0}
    try:
        User.objects.get(email=email)
        data["message"] = "This Email is exist"
        return Response(data)
    except:
        pass
    try:
        User.objects.get(username=username)
        data["message"] = "This username is exist"
        return Response(data)
    except:
        pass

    user = User.objects.create(username=username, email=email, password=passwd)
    user.last_name = ''
    user.first_name = user.username
    if designation == 'student':
        student = Student(user=user)
        student.save()
        user.set_password(passwd)
        user.save()
        data["success"] = 1
    return Response(data)


student.signup = signup


@api_view(["POST"])
def login(req):
    # if req.data['designation'] == 'student':
    data = {'success': 0}
    if 'email' in req.data.keys():
        user = User.objects.get(email=req.data['email'])
    elif 'username' in req.data.keys():
        user = User.objects.get(username=req.data['username'])
    else:
        data['message'] = 'can\'t find any account'
        return Response(data)
    password = req.data['passwd']

    if not user.check_password(password):
        data['message'] = 'Wrong Password'
        return Response(data)
    # Now we can login

    data['success'] = 1
    return Response(data)


student.login = login


@api_view(["POST"])
def profile(req):
    data = dict(req.data)
    print(data)
    if 'email' in req.data.keys():
        user = User.objects.get(email=req.data['email'])
    elif 'username' in req.data.keys():
        user = User.objects.get(username=req.data['username'])
    else:
        return Response({'error': True})
    print(user)
    password = req.data['passwd']
    if user.check_password(password):
        print("FFFFFFFFFFFFFFFFFF")
        # print(req.data["update"])
        if data["update"] == False:
            data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'roll_no': user.student.roll_no,
                'department': user.student.department,
                # 'contuct_no': user.student.contuct_no,

            }
            print(data)
            return Response(data)
        else:
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.student.roll_no = data['roll_no']
            user.student.department = data['department']
            # user.student.contuct_no = req.data['contuct_no']
            user.student.save()
            user.save()

        return Response({'message': 'successful'})
    return Response({'error': True})


student.profile = profile


@api_view(["GET", "POST"])
def home(req):
    return Response()
