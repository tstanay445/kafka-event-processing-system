from message.models import Message
from message.serializers import MessageSerializer,UserSerializer,RegisterSerializer
from rest_framework import generics,permissions,viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from message.permissions import IsOwnerOrReadOnly
from .kafka_producer import send_message_created
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):

        message_text = request.data.get("message")

        send_message_created(request.user.username, message_text)

        return Response(
            {"status": "message event sent to Kafka"},
            status=status.HTTP_202_ACCEPTED
        )

        

from django.contrib.auth.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
@api_view(['GET'])
def api_root(request,format = None):
    return Response(
        {
            'users' : reverse('user-list',request = request,format = format),
            'message' : reverse('messages-list',request = request,format = format)
        }
    )
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

from .serializers import LoginSerializer
class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        return Response({
            "message": f"Welcome {user.username}"
        })
