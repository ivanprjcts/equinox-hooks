from rest_framework import viewsets, filters

from hooks.models import (
    Application, Hook, Request, Header
)
from hooks.serializers import (
    ApplicationSerializer, HookSerializer, RequestSerializer, HeaderSerializer
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


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class HeaderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
