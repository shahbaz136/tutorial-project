from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from tutorial_api.models import Author, Publisher
from tutorial_api.serializers import AuthorResponse, AuthorRequest, AuthorCreateResponse, AuthorUpdateRequest, PublisherAuthorRequest
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


class AuthorView(APIView):

    def get(self, request):
        queryset = Author.objects.all()
        response = AuthorResponse(instance=queryset, many=True)
        return Response(response.data)

    def post(self, request):
        request_data = request.data
        req = PublisherAuthorRequest(data=request_data)

        validation = req.is_valid(raise_exception=True)
        print("-----validation----", validation)
        request_valid_data = req.validated_data
        print("----request_valid_data---", request_valid_data)

        publisher_data = {}
        author_data = {}
        list1 = ['name', 'address', 'city', 'state_province', 'country', 'website']
        list2 = ['first_name', 'last_name', 'email']
        for item in request_valid_data:
            if item in list1:
                publisher_data[item] = request_valid_data[item]
            if item in list2:
                author_data[item] = request_valid_data[item]

        response_data = {'success':False}

        Author.objects.create(
            **author_data
        )
        Publisher.objects.create(
            **publisher_data
        )
        response_data['message'] = "author created"
        response_data["success"] = True
        response = AuthorCreateResponse(data=response_data)
        validation = response.is_valid(raise_exception=True)
        return Response(response.validated_data, status=status.HTTP_201_CREATED)


    def put(self, request, aid):
        request_data = request.data
        req = AuthorUpdateRequest(data=request_data)
        validation = req.is_valid(raise_exception=True)
        request_valid_data = req.validated_data

        response_data = {'success':False}


        Author.objects.filter(id=aid).update(
            **request_valid_data
        )

        response_data['message'] = "author upadted"
        response_data["success"] = True
        response = AuthorCreateResponse(data=response_data)
        validation = response.is_valid(raise_exception=True)

        return Response(response.validated_data, status=status.HTTP_201_CREATED)




