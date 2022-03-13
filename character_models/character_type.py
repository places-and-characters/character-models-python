from enum import Enum
import json


class CharacterType():
    def __init__(self):
        self.id = None
        self.name = None

    def __str__(self) -> str:
        return json.dumps(self)

    @staticmethod
    def from_json(json_obj: json) -> CharacterType:
        c_type = CharacterType()
        c_type = json_obj['id']
        c_type = json_obj['name']
        return c_type
