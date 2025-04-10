from rest_framework import serializers

from rest_framework import serializers

class CreditJournalEntrySerializer(serializers.Serializer):
    datetime = serializers.CharField(max_length = 255)  # Add a datetime field
    bill_id = serializers.CharField(max_length=255)
    user = serializers.CharField(max_length=255)
    debit_ledgers = serializers.ListField(child=serializers.CharField(allow_null=True), required=False)
    debit_ledger_names = serializers.ListField(child=serializers.CharField(allow_null=True), required=False)
    # debit_ledger_names = serializers.CharField(max_length= 255)   
    debit_particulars = serializers.ListField(child=serializers.CharField(allow_null=True), required=False)
    debit_amounts = serializers.ListField(child=serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True))
    debit_subledgers = serializers.ListField(child=serializers.CharField(allow_null=True), required=False)
    
    credit_ledgers = serializers.ListField(child=serializers.CharField(allow_null=True), required=False)
    credit_particulars = serializers.ListField(child=serializers.CharField(allow_null=True), required=False)
    credit_amounts = serializers.ListField(child=serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True))
    credit_subledgers = serializers.ListField(child=serializers.CharField(allow_null=True), required=False)
    outlet_name = serializers.CharField(max_length = 255)
