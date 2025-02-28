from rest_framework import viewsets
from rest_framework import serializers
from people.models.people import Person
from django.contrib.auth.hashers import make_password


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Extract fields needed for create_user
        email = validated_data.get('email')
        name = validated_data.get('name')
        password = validated_data.get('password')
        groups = validated_data.pop('groups', None)
        user_permissions =  validated_data.pop('user_permissions', None)

        # for field in ['email', 'name', 'password']:
        #     if field in validated_data:
        #         validated_data.pop(field)

        user = Person.objects.create_user(
            email=email,
            name=name,
            password=password
        )

        if groups is not None:
            user.groups.set(groups)
        
        if user_permissions is not None:
            user.user_permissions.set(user_permissions)

        user.save()

        return user

    def update(self, instance, validated_data):
        # Handle password updates properly
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        if 'groups' in validated_data:
            groups = validated_data.pop('groups')
            instance.groups.set(groups)

        if 'user_permissions' in validated_data:
            permissions = validated_data.pop('user_permissions')
            instance.user_permissions.set(permissions)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = Person.USERNAME_FIELD

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name
        token['email'] = user.email
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer