from rest_framework import serializers


class StoreSerializer(serializers.Serializer):
    quantity = serializers.CharField(max_length=100)
    description = serializers.CharField()
    