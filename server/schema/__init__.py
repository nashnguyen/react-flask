from graphene import ObjectType, Schema, relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import Salary as SalaryModel


class Salary(SQLAlchemyObjectType):
    class Meta:
        model = SalaryModel
        interfaces = (relay.Node,)


class Query(ObjectType):
    node = relay.Node.Field()
    all_salaries = SQLAlchemyConnectionField(Salary.connection)


schema = Schema(query=Query)
