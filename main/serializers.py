from rest_framework import serializers
from .models import Contact, Product

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'company', 'email', 'mobile', 'message', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'short_description',
            'full_description',
            'icon',
            'specifications',
            'applications',
            'key_features',
            'technical_details',
            'created_at',
        ]
