from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'full_name', 'phone', 'address', 'city', 'state', 'country', 'pincode', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = CustomUser.objects.filter(email=email).first()

            if user:
                if not user.check_password(password):
                    raise serializers.ValidationError({'email': 'Incorrect email or password'})
            else:
                raise serializers.ValidationError({'email': 'User not found'})
        else:
            raise serializers.ValidationError({'email': 'Email and password are required'})

        attrs['user'] = user
        return attrs