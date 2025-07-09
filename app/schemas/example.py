from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, constr


class ExampleType(str, Enum):
    EXAMPLE_TYPE_1 = 'example_type_1'
    EXAMPLE_TYPE_2 = 'example_type_2'


class ExampleBase(BaseModel):
    name: constr(max_length=256)
    description: constr(max_length=2048)
    example_type: ExampleType


class ExampleCreate(ExampleBase):
    pass


class ExampleUpdate(ExampleBase):
    pass


class Example(ExampleBase):
    id: UUID  # noqa: A003

    model_config = ConfigDict(from_attributes=True)
