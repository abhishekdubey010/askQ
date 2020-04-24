from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Account
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST', 'GET'])
def registration_view(request):

    if request.method == 'GET':
        register_object = Account.objects.all()
        register_serializer = RegistrationSerializer(register_object, many=True)
        return Response(register_serializer.data)

    if request.method == 'POST':
        register_serializer = RegistrationSerializer(data=request.data)
        data = {}
        if register_serializer.is_valid():
            account = register_serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = register_serializer.errors
        return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete.
    """
    try:
        snippet = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistrationSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegistrationSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)