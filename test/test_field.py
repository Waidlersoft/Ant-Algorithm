from .algorithm.fieldpreparation import FieldPreparation
import .algorithm.config as config

def test_start():
    playingField = FieldPreparation.create_field()
    x_border = config.x_border
    y_border = config.y_border
    assert isinstance(playingField, dict) == True
    assert len(playingField) == (x_border[1]-x_border[0]+1)*(y_border[1]-y_border[0]+1)
    for square in playingField:
        for index in ["border", "search", "return"]:
            assert (playingField[square][index] == 0 or playingField[square][index] == 1) == True

def test_wind():
    assert FieldPreparation.wind() == False