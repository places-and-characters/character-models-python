from character_models.character_type import CharacterType
import json


class Character:
    def __init__(self):
        self.id = None
        self.type = None
        self.player_name = None
        self.name = None
        self.experience_points = None

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def validate(self, raise_exception=False):
        if not Character._validate_field(self.id, 'id', raise_exception):
            return False
        if not Character._validate_field(self.type, 'type', raise_exception):
            return False
        if not Character._validate_field(self.name, 'name', raise_exception):
            return False
        if not Character._validate_field(
                self.experience_points, 'experience points', raise_exception):
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
        c = Character()
        if 'id' in obj:
            c.id = obj['id']
        if 'type' in obj:
            c.type = CharacterType.from_json(obj['type'])
        if 'player_name' in obj:
            c.player_name = obj['player_name']
        if 'name' in obj:
            c.name = obj['name']
        if 'experience_points' in obj:
            c.experience_points = obj['experience_points']
        c.validate(raise_exception=True)
        return c
