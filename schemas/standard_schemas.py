from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, PositiveInt
from pydantic.alias_generators import to_camel

character_json = {
    "characterType": "person",
    "name": "Mads",
    "email": "test@test.com",
    "age": "34",
    "address": {"street": "1234 Main St", "city": "Anytown", "state": "TX"},
}


class CharacterType(StrEnum):
    """Character type enum"""

    person = "person"
    animal = "animal"


class Address(BaseModel):
    """Address schema"""

    street: str
    city: str
    state: str


class Character(BaseModel):
    """Character schema"""

    model_config = ConfigDict(alias_generator=to_camel)

    character_type: CharacterType
    name: str
    email: EmailStr
    age: PositiveInt
    address: Address

    def get_city(self):
        return self.address.city


character = Character(**character_json)
print(character.get_city())
