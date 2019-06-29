import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
#from django.db.models import Q

from .models import DocxFile as Docx

class DocxType(DjangoObjectType):
    class Meta:
        model = Docx


class Query(graphene.ObjectType):
    docxs = graphene.List(DocxType)

    def resolve_docxs(self, info):
        return Docx.objects.all()


class CreateDocx(graphene.Mutation):
    docx = graphene.Field(DocxType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, title, description):

        user = info.context.user
        if user.is_anonymous:
                    raise GraphQLError('Log in to manipulate docx file.')

        docx = Docx(title=title, description=description, created_by=user)
        docx.save()
        return CreateDocx(docx=docx)


class Mutation(graphene.ObjectType):
    create_docx = CreateDocx.Field()

