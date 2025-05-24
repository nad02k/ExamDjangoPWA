import graphene
from graphene_django import DjangoObjectType
from assets.models import OfflineAsset

class OfflineAssetType(DjangoObjectType):
    class Meta:
        model = OfflineAsset

class Query(graphene.ObjectType):
    assets = graphene.List(OfflineAssetType)

    def resolve_assets(self, info):
        return OfflineAsset.objects.all()

schema = graphene.Schema(query=Query)