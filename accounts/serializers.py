from dataclasses import fields
from rest_framework import serializers
from .models import Account

class SerializerAccounts(serializers.ModelSerializer):
    class Meta:
        models = Account
        fields = ["username","email","first_name","last_name","cellphone","is_staff"]
        read_only_fields  = ['date_joined' , 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}
        
        def create(self, validate_data: dict):
            create_user = Account.objects.create_user(**validate_data)
            return create_user

