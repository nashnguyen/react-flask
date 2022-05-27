from graphene import List, ObjectType, Schema
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Salary as SalaryModel


class Salary(SQLAlchemyObjectType):
    class Meta:
        model = SalaryModel


class Query(ObjectType):
    salaries = List(Salary)

    def resolve_salaries(self, info):
        return Salary.get_query(info).all()


schema = Schema(query=Query)
