import json
from character_models.character_type import CharacterType


class Character:
    def __init__(self):
        self.id = None
        self.type = None
        self.player_name = None
        self.name = None
        self.experience_points = None

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_obj: json):
        c = Character()
        c.id = json_obj['id']
        if json_obj['type']:
            c.type = CharacterType.from_json(json_obj['type'])
        else:
            raise Exception('Character Type not provided')
        c.player_name = json_obj['player_name']
        c.name = json_obj['name']
        c.experience_points = json_obj['experience_points']
        return c
