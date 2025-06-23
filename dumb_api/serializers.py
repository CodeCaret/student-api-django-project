from rest_framework import serializers
from dumb_api.models import StudentDetail

class StudentDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 20)
    age = serializers.IntegerField(min_value = 0)
    course = serializers.CharField()

    def create(self, validated_data):
        return StudentDetail.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.course = validated_data.get('course', instance.course)
        instance.save()
        return instance