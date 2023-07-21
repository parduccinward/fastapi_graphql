import uuid
import strawberry
import typing
from models.user import users


@strawberry.type
class User:
    id: str
    name: str
    email: str


@strawberry.type
class Queries:
    @strawberry.field
    def user(self, info, id: int) -> User:
        return users.find_one({"id": id})

    @strawberry.field
    def users(self, info) -> typing.List[User]:
        return users.find({})


@strawberry.type
class Mutations:
    @strawberry.mutation
    def create_user(self, info, name: str, email: str) -> User:
        unique_id = str(uuid.uuid4())
        user = User(id=unique_id, name=name, email=email)
        users.insert_one(user)
        return user

    @strawberry.mutation
    def update_user(self, info, id: int, name: str, email: str) -> User:
        user = User(id=id, name=name, email=email)
        users.update_one({"id": id}, {"$set": user})
        return user

    @strawberry.mutation
    def delete_user(self, info, id: int) -> bool:
        users.delete_one({"id": id})
        return True
