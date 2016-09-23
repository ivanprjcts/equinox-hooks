from django.views import View
from django.http import HttpResponse

from rest_framework.decorators import detail_route
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from rest_framework.response import Response

from hooks.models import (
    Application, Hook, Header
)
from hooks.serializers import (
    ApplicationSerializer, HookSerializer, HeaderSerializer
)
from hooks.filters import HookFilter
from hooks.latchapi import Latch


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    @detail_route(methods=['post'])
    def pair(self, request, pk=None, **kwargs):
        token = request.data.get('token', None)
        app = Application.objects.get(pk=pk)
        app_id = app.app_id
        secret = app.secret
        api = Latch(app_id, secret)
        if token:
            res = api.pair(token)
            if "data" in res.data and "accountId" in res.data["data"]:
                app.account_id = res.data["data"]["accountId"]
                app.save()
        serializer = ApplicationSerializer(app)
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def unpair(self, request, pk=None, **kwargs):
        app = Application.objects.get(pk=pk)
        app_id = app.app_id
        secret = app.secret
        account_id = app.account_id
        api = Latch(app_id, secret)
        api.unpair(account_id)
        app.account_id = None
        app.save()
        serializer = ApplicationSerializer(app)
        return Response(serializer.data)


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


class LatchHookListener(View):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def get(self, request, format=None):
        challenge = self.request.GET.get('challenge', "123456")
        if challenge:
            return HttpResponse(challenge, content_type="text/plain")

        # execute my code
        return HttpResponse(challenge, content_type="text/plain")
