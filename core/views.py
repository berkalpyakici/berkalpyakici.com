import os
import logging
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import SocialSerializer
from .models import Social


class SocialView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    
    # Initializing the serializer
    serializer_class = SocialSerializer

    # Setting the permission
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Setting the queryset
    queryset = Social.objects.all().order_by('-id')


class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    build`).
    """
    index_file_path = os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')

    def get(self, request):
        try:
            with open(self.index_file_path) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead after
                running `yarn start` on the frontend/ directory
                """,
                status=501,
            )