from accounts.serializers import SerializerAccounts
from rest_framework import generics
from .models import Account

# Create your views here.
class AccountView(generics.ListCreateAPIView):

    queryset = Account.objects.all()
    serialzier_class = SerializerAccounts
    
    
class AcccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Account.objects.all()
    serialzier_class = SerializerAccounts
    