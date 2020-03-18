import config,re

def test_direction():
    assert isinstance(config.direction, list) == True
    assert len(config.direction) == 8
    for i in range(0, 8):
        assert isinstance(config.direction[i], list) == True

def test_startpoint():
    assert isinstance(config.startpoint, str) == True
    assert len(config.startpoint) == 6
    assert bool(re.match(r'6*[0-9]',config.startpoint)) == True

def test_startpoint():
    assert isinstance(config.targetpoint, str) == True
    assert len(config.targetpoint) == 6
    assert bool(re.match(r'6*[0-9]',config.targetpoint)) == True