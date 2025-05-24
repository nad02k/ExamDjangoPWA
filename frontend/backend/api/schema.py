import graphene
from graphene_django import DjangoObjectType
from assets.models import OfflineAsset
from subscriptions.models import PushSubscription

class OfflineAssetType(DjangoObjectType):
    class Meta:
        model = OfflineAsset

class PushSubscriptionType(DjangoObjectType):
    class Meta:
        model = PushSubscription

class Query(graphene.ObjectType):
    offline_assets = graphene.List(OfflineAssetType)

    def resolve_offline_assets(root, info):
        return OfflineAsset.objects.all()

schema = graphene.Schema(query=Query)