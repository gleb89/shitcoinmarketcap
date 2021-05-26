from rest_framework import serializers

from .models import Comments


class RecursiveSerializer(serializers.Serializer):
    """

    Вывод рекурсивно children

    """

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class FilterReviewListSerializer(serializers.ListSerializer):
    """

    Фильтр комментариев, только parents
    
    """

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentsSerializer(serializers.ModelSerializer):

    children = RecursiveSerializer(many=True, allow_null=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Comments
        fields = '__all__'
