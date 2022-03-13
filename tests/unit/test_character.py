import pytest
from character_models.character import Character
from character_models.character_type import CharacterType


def test_character(mocker):
    # setup
    c = Character()
    c.id = "testid"
    c_type = CharacterType()
    c_type.id = "testtypeid"
    c_type.name = "test type name"
    c.type = c_type
    c.player_name = "test player name"
    c.name = "test name"
    c.experience_points = 2022
    expected = '{"id": "testid", "type": {"id": "testtypeid", "name": "test type name"}, "player_name": "test player name", "name": "test name", "experience_points": 2022}'

    # exercise
    actual = str(c)

    # verify
    assert actual == expected


def test_character_from_json(mocker):
    # setup
    obj_type = {}
    obj_type['id'] = "testtypeid"
    obj_type["name"] = "test type name"

    obj = {}
    obj['id'] = "testid"
    obj['type'] = obj_type
    obj["player_name"] = "test player name"
    obj["name"] = "test name"
    obj["experience_points"] = 2022

    # exercise
    actual = Character.from_json(obj)

    # verify
    assert actual != None
    assert isinstance(actual, Character)
    assert actual.id == "testid"
    assert actual.type.id == "testtypeid"
    assert actual.type.name == "test type name"
    assert actual.name == "test name"
    assert actual.player_name == "test player name"
    assert actual.experience_points == 2022
