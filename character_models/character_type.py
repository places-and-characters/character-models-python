from enum import Enum
import json


class CharacterType():
    def __init__(self):
        self.id = None
        self.name = None

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def validate(self, raise_exception=False):
        if not CharacterType._validate_field(self.id, 'id', raise_exception):
            return False
        if not CharacterType._validate_field(self.name, 'name', raise_exception):
            return False
        return True

    @staticmethod
    def _validate_field(field, name, raise_exception=False):
        if field == None:
            if raise_exception:
                raise KeyError('%s is None' % name)
            return False
        return True

    @staticmethod
    def from_json(obj: json):
        c_type = CharacterType()
        if 'id' in obj:
            c_type.id = obj['id']
        if 'name' in obj:
            c_type.name = obj['name']
        c_type.validate(raise_exception=True)
        return c_type
