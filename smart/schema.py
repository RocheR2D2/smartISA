import graphene
import docxs.schema, users.schema, case.schema
import graphql_jwt


class Query(users.schema.Query, docxs.schema.Query, case.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, docxs.schema.Mutation, case.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
