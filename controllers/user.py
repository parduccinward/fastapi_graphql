from fastapi import APIRouter
import strawberry
from strawberry.asgi import GraphQL

from app_types.user import Queries, Mutations

user = APIRouter()
schema = strawberry.Schema(Queries, Mutations)
graphql_app = GraphQL(schema)
user.add_route("/graphql", graphql_app)
