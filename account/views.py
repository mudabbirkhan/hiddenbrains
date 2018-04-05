from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer, ChangePasswordSerialzer
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from rest_framework import status
from django.shortcuts import render, redirect
from rest_framework import permissions
from django.views.generic import View, TemplateView
from .models import User
from django.contrib.auth import logout


class LoginAPI(APIView):
    # authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    serializer_class = LoginSerializer

    # permission_classes = permissions.IsAuthenticated,

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)
            if user:
                login(request, user)
                return Response({'msg': 'User is Logged-in'}, status=status.HTTP_302_FOUND)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterAPI(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPI(APIView):
    permission_classes = permissions.IsAuthenticated,
    serializer_class = ChangePasswordSerialzer

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerialzer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'msg': 'Password has been changed'}, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'account/dashboard.html', context={'user': request.user})
        return render(request, 'account/login.html', context={'error': None})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'account/dashboard.html', context={'user': user})
        else:
            return render(request, 'account/login.html', context={'error': 'Invalid Credentials'})


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'account/dashboard.html', context={'user': request.user})
        return render(request, 'account/register.html', context={'error': None})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        mobile_no = request.POST['mob_number']

        try:

            user, created = User.objects.get_or_create(username=username, first_name=name, email=email, address=address,
                                                       mobile_no=mobile_no)
        except:
            created = False
        if created:
            user.set_password(password)
            user.save()
            login(request, user)
            return render(request, 'account/dashboard.html', context={'user': user})
        else:
            return render(request, 'account/register.html', context={'error': 'Error while Registering'})


def logout_view(request):
    logout(request)
    return redirect('index')


class IndexView(TemplateView):
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['msg'] = None
        return context


class ChangePasswordView(View):
    def get(self, request):
        return render(request, 'account/change_password.html', context={'error': None})

    def post(self, request):
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']

        if not request.user.check_password(old_password):
            return render(request, 'account/change_password.html', context={'error': 'Wrong Old Password'})
        request.user.set_password(new_password)
        request.user.save()
        return render(request, 'account/index.html', context={'msg': 'Password Changed'})
