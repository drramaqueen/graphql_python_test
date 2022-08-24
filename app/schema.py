import graphene
from app.objectmgr import ObjectMgr


mgr = ObjectMgr.get_manager_instance(5)


class Query(graphene.ObjectType):
    number = graphene.Int()
    is_empty = graphene.Boolean()
    available_count = graphene.Int()

    @staticmethod
    def resolve_number(self, info):
        return mgr.get_object().get_value()

    @staticmethod
    def resolve_is_empty(self, info):
        return mgr.is_empty()

    @staticmethod
    def resolve_available_count(self, info):
        return mgr.available_count()


class FreeObject(graphene.Mutation):
    class Arguments:
        number = graphene.Int()
    number = graphene.Field(graphene.Int)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, number):
        mgr.free_object(number)
        ok = True
        return FreeObject(number=number, ok=ok)


class GetObject(graphene.Mutation):
    number = graphene.Field(graphene.Int)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info):
        number = mgr.get_object().get_value()
        ok = True
        return FreeObject(number=number, ok=ok)


class Mutations(graphene.ObjectType):
    free_object = FreeObject.Field()
    get_object = GetObject.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
