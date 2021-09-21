from rest_framework import serializers
from authentication.models import transactions

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = transactions 
        fields=('transactionId','transactionName')

