from rest_framework import mixins, generics
from django.shortcuts import render
from  .models import carModel, CarSerializer


# Create your views here.
'''
____________Mixin Classes and action methods____________
        ListModelMixin      ---- list()
        CreateModelMixin    ---- create()
        RetriveModelMixin   ---- retrieve()
        DestroyModelMixin   ---- destroy()
        UpdateModelMixin    ---- update()
___________Handler Method_________________
   from GenericApiView we will get get(),put(),post(),delete()
   
'''


class CarListView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
        queryset = carModel.objects.all()
        serializer_class  = CarSerializer
        
        def get(self, request):
                return self.list(request)
        
        def post(self, request):
                return self.create(request)

class CarDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
        queryset = carModel.objects.all()
        serializer_class  = CarSerializer
        def get(self, request, pk):
                return self.retrieve(request, pk)
        # to access one use Retrive
        
        def put(self, request, pk):
                return self.update(request, pk)
        
        def delete(self, request, pk):
                return self.destroy(request, pk)
    