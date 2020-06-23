from rest_framework.viewsets import ModelViewSet
from ghostpostapi.serializers import RoastandBoastSerializer
from ghostpostapi.models import RoastsAndBoasts
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class postsViewSet(ModelViewSet):
    serializer_class = RoastandBoastSerializer
    queryset = RoastsAndBoasts.objects.all()

    @action(detail=False)
    def Boasts(self,request):
        SortUpVotes = RoastsAndBoasts.objects.filter(roastorboast="B")
        serializer = self.get_serializer(SortUpVotes, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def Roasts(self,request):
        SortdownVotes = RoastsAndBoasts.objects.filter(roastorboast="R")
        serializer = self.get_serializer(SortdownVotes, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def mostPopular(self,request):
        Sortscore = RoastsAndBoasts.objects.order_by('-score')
        serializer = self.get_serializer(Sortscore, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def leastPopular(self,request):
        Sortscore = RoastsAndBoasts.objects.order_by('score')
        serializer = self.get_serializer(Sortscore, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def upVote(self, request, pk=None):
        post = self.get_object()
        post.upVotes += 1
        post.score += 1
        post.save()
        return Response({'status': 'Upvote success'})

    @action(detail=True, methods=['post'])
    def downVote(self, request, pk=None):
        post = self.get_object()
        post.downVotes -= 1
        post.score -= 1
        post.save()
        return Response({'status': 'Downvote success'})