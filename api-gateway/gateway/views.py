# -*- coding: utf-8 -*-

import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_proxy.views import ProxyView


class PostsAPIProxyView(ProxyView):

    proxy_host = settings.MICROSERVICES.get("PostsMicroservice")
    source = "1.0/posts/"
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        Antes de mandar la peticion al microservicio, añade la informacion del usuario autenticado
        """
        url = self.get_request_url(request)
        data = {
            "user_id": request.user.pk,
            "description": request.data.get("description")
        }
        files = self.get_request_files(request)

        # lanzamos la peticion HTTP al API REST del Microservicio
        response = requests.post(url, data, files=files)

        return Response(response.json(), response.status_code)
