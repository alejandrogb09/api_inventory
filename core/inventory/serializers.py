from rest_framework import serializers
from .models import Product, Movement

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'stock',
            'is_active',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

class MovementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movement
        fields = [
            'id',
            'product',
            'movement_type',
            'quantity',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "La cantidad debe ser mayor a cero."
            )
        return value
    
    def validate(self, data):
        product = data['product']
        movement_type = data['movement_type']
        quantity = data['quantity']

        if movement_type == Movement.EXIT and product.stock < quantity:
            raise serializers.ValidationError(
                "Stock insuficiente para realizar salida."
            )
        
        return data
    
    def create(self, validated_data):
        product = validated_data['product']
        movement_type = validated_data['movement_type']
        quantity = validated_data['quantity']

        if movement_type == Movement.ENTRY:
            product.stock += quantity
        else:
            product.stock -= quantity

        product.save()

        return super().create(validated_data)