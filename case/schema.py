import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

from .models import Case

class CaseType(DjangoObjectType):
    class Meta:
        model = Case


class Query(graphene.ObjectType):
    cases = graphene.List(CaseType, search=graphene.String())

    def resolve_cases(self, info, search=None):
        if search:
            filter = (
                Q(casetitle__icontains=search)
            )
            return Case.objects.filter(filter)

        return Case.objects.all()


class CreateCase(graphene.Mutation):
    case = graphene.Field(CaseType)

    class Arguments:
        casetitle = graphene.String()
        casetitle_long = graphene.String()
        arbitration_rules = graphene.String()
        decisions_rendered = graphene.String()
        link = graphene.String()

    def mutate(self, info, casetitle, casetitle_long, arbitration_rules, decisions_rendered, link):

        case = Case(casetitle=casetitle, casetitle_long=casetitle_long, arbitration_rules=arbitration_rules, decisions_rendered=decisions_rendered, link=link)
        case.save()
        return CreateCase(case=case)


class Mutation(graphene.ObjectType):
    create_case = CreateCase.Field()

