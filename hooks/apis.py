from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from hooks.models import (
    Application, Hook, Header
)
from hooks.serializers import (
    ApplicationSerializer, HookSerializer, HeaderSerializer
)
from hooks.filters import HookFilter


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class HookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Hook.objects.all()
    serializer_class = HookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = HookFilter


class HeaderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class LatchHookListener(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        challenge = self.request.query_params.get('challenge', "123456")
        return Response({"challenge": challenge})

