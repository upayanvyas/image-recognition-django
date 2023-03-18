from rest_framework import serializers
from image_recognition.models.image_model import ImageModel

class MyImageSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = ImageModel
        fields = ('id', 'name', 'image')
