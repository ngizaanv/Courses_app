from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ['id', 'name', 'imgpath']

class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ['id', 'latitude', 'longitude', 'address']

class ContactSerializer(serializers.ModelSerializer):


    class Meta:
        model = Contact
        fields = ['id', 'type', 'value']


class CourseSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category', 'logo', 'contacts', 'branches']

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        course = Course.objects.create(**validated_data, category=category)

        for contact_data in contacts_data:
            Contact.objects.create(course=course, **contact_data)
        for branch_data in branches_data:
            Branch.objects.create(course=course, **branch_data)
        return course

