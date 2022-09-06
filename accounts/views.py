from accounts.serializers import SerializerAccounts
from rest_framework import generics
from .models import Account
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateAndDelete


# Create your views here.
class AccountView(generics.ListCreateAPIView):

    queryset = Account.objects.all()
    serializer_class = SerializerAccounts
    
    
class AcccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]        
    permission_classes = [ UpdateAndDelete]    
    queryset = Account.objects.all()
    serializer_class = SerializerAccounts
    
    