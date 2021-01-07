from rest_framework import serializers
from todo.models import Todo
from .utils import DateTimeFieldUtils


class TodoSerializer(serializers.ModelSerializer, DateTimeFieldUtils):
    author = serializers.StringRelatedField()

    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = ["author"]

    def to_representation(self, instance):
        representation = super(TodoSerializer, self).to_representation(instance)
        timestr = self.datetimefilter(instance.date)
        representation["date"] = instance.date.strftime(timestr)
        return representation
