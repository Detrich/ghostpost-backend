from rest_framework.serializers import ModelSerializer
from ghostpostapi.models import  RoastsAndBoasts


class RoastandBoastSerializer(ModelSerializer):
    class Meta:
        model = RoastsAndBoasts
        basename = 'RandB'
        fields = (
            'roastorboast',
            'content',
            'upVotes',
            'downVotes',
            'createdAt',
            'score',
            'id'
        )
