# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render
from django.views import View

from django.conf import settings


class PostsListView(View):

    def get(self, request):

        # obtener los posts del microservicio de posts
        url = settings.MICROSERVICES.get("PostsMicroservice") + "/1.0/posts/"
        response = requests.get(url)

        # TODO: controlar posibles errores de comuniacion al llamar al microservicio
        posts = response.json()

        # crear un contexto
        context = {
            "posts": posts
        }

        # renderizar la plantilla
        return render(request, "posts_list.html", context)
