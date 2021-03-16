from rest_framework import serializers


#-----------request serializer---------------

class AuthorRequest(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(allow_null=True, allow_blank=True, required=False)

class AuthorUpdateRequest(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(allow_null=True, allow_blank=True, required=False)

class PublisherAuthorRequest(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=60)
    state_province = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=50)
    website = serializers.URLField()

    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=40)
    email = serializers.CharField(allow_null=True, allow_blank=True)

#------------response serializer----------------

class AuthorResponse(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()


class AuthorCreateResponse(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField(allow_null=True, allow_blank=True, required=False)
