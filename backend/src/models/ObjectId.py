from bson import ObjectId as BsonObjectId
from bson.errors import InvalidId
from pydantic import BaseConfig, BaseModel
from pydantic import Field as PydanticField


class ObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")
