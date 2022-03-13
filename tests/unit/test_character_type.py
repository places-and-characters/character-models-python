import pytest
from character_models.character_type import CharacterType


def test_character_type(mocker):
    # setup
    c_type = CharacterType()
    c_type.id = "testid"
    c_type.name = "test name"
    expected = '{"id": "testid", "name": "test name"}'

    # exercise
    actual = str(c_type)

    # verify
    assert actual == expected


def test_character_type_from_json(mocker):
    # setup
    obj = {}
    obj['id'] = "testid"
    obj["name"] = "test name"

    # exercise
    actual = CharacterType.from_json(obj)

    # verify
    assert actual != None
    assert isinstance(actual, CharacterType)
    assert actual.id == "testid"
    assert actual.name == "test name"
