from rest_framework.exceptions import ValidationError

from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    subtitle = serializers.CharField(max_length=200)
    content = serializers.CharField()
    author = serializers.CharField(max_length=100)
    isbn = serializers.CharField(max_length=13)
    price = serializers.DecimalField(max_digits=300, decimal_places=2)

    def create(self, validated_data):
        title = validated_data.get("title", None)
        if not title.isalpha():
            raise ValidationError({"msg": "Sarlavha harflardan iborat bo'ladi"})
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.select_book = validated_data["select_book"]
        instance.save()



    # class Meta:
    #     model=Book
    #     fields=("id","content","title","subtitle","author","isbn","price",)

    # def validate(self,data):
    #     title=data.get("title",None)
    #     if not title.isalpha():
    #         raise ValidationError({"msg":"Sarlavha harflardan iborat bo'ladi"})
    #
    #     return data