from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly
from .serializers import UserFavSerializer, UserFavDetailSerializer, AddressSerializer, LeavingMessageSerializer
from .models import UserFav, UserLeavingMessage, UserAddress

class UserFavViewset(viewsets.ReadOnlyModelViewSet,mixins.CreateModelMixin, mixins.DestroyModelMixin):
    """
       list:
           获取用户收藏列表
       retrieve:
           判断某个商品是否已经收藏
       create:
           收藏商品
       """
    #权限
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)#验证当前用户
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)#局部session
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer

        return UserFavSerializer


class LeavingMessageViewset(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言功能
    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = LeavingMessageSerializer

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class AddressViewset(viewsets.ModelViewSet):
    '''
    收货地址
    list:
        获取address
    create：
        添加

    '''