from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from image_recognition.serielizers.image_serielizer import MyImageSerializer
from image_recognition.models.image_model import ImageModel

from django.http import HttpResponse


class UserImage(APIView):

    def get(self, request):
        try:
            images = []
            if request.GET['id']:
                image = ImageModel.objects.get(pk=request.GET['id'])
                print("images ===> : ", image.image)
                response = HttpResponse(image, content_type='image/jpeg')
                response['Content-Disposition'] = 'attachment; filename="%s"' % str(image.image)
                # images = MyImageSerializer(images, many=True)
                # print("serialized images ===> : ",images.data)
                print("response ======> ", response)
                return Response({"msg": 'get Success', "data": response})
            else:
                print('no id')
                images = ImageModel.objects.all()
                images = MyImageSerializer(images, many=True).data
                return Response({"msg": 'get Success', "data": images})
        except Exception as e:
            print("Error : ", e)
            return Response({"msg": 'get Success', "data": images})

    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        print("To access payload : ", request.data)
        serializer = MyImageSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
