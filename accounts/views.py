from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,status
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetView,PasswordResetConfirmView
from accounts.serializers import CustomUserSerializer
from delivery.models import Store
from delivery.serializers import StoreSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404



# Create your views here.

class CustomRegisterView(RegisterView):
    pass


class CustomVerifyEmailView(VerifyEmailView):
    pass


class CustomLoginView(LoginView):
    pass
   


class CustomLogoutView(LogoutView):
    pass


class CustomPasswordChangeView(PasswordChangeView):
    pass


class CustomPasswordResetView(PasswordResetView):
    pass

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    pass


class UserProfileView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


    @action(detail=True, methods=['post'])
    def add_favorite_store(self, request, pk=None):
        user = self.get_object()
        store_id = request.data.get('store_id')

        if store_id:
            store = get_object_or_404(Store, pk=store_id)
            user.favorite_stores.add(store)
            user.save()
            return Response({'detail': 'Store added to favorites'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Store ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
        

    
    @action(detail=True, methods=['post'])
    def remove_favorite_store(self, request, pk=None):
        user = self.get_object()
        store_id = request.data.get('store_id')

        if store_id:
            store = get_object_or_404(Store, pk=store_id)
            user.favorite_stores.remove(store)
            user.save()
            return Response({'detail': 'Store removed from favorites'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Store ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=True, methods=['get'])
    def favorite_stores(self, request, pk=None):
        user = self.get_object()
        favorite_stores = user.favorite_stores.all()
        serializer = StoreSerializer(favorite_stores, many=True, context={'request': request})  
        return Response(serializer.data, status=status.HTTP_200_OK)    

    