import syspath, re
import algorithm.config as config
from algorithm.common import common

def test_direction():
    assert isinstance(config.direction, list) is True
    assert len(config.direction) == 8
    for i in range(0, 8):
        assert isinstance(config.direction[i], list) is True
        assert len(config.direction[i]) == 2
        assert config.direction[i][0] in [-1, 0, 1]
        assert config.direction[i][1] in [-1, 0, 1]

def test_startpoint():
    x_y_List = common.xy_pos(config.startpoint)
    assert isinstance(config.startpoint, str) is True
    assert len(config.startpoint) == 6
    assert bool(re.match(r"6*[0-9]",config.startpoint)) is True
    assert (x_y_List[0] > config.x_border[0]) is True
    assert (x_y_List[0] < config.x_border[1]) is True
    assert (x_y_List[1] > config.y_border[0]) is True
    assert (x_y_List[1] < config.y_border[1]) is True

def test_targetpoint():
    x_y_List = common.xy_pos(config.targetpoint)
    assert isinstance(config.targetpoint, str) is True
    assert len(config.targetpoint) == 6
    assert bool(re.match(r"6*[0-9]",config.targetpoint)) is True
    assert (x_y_List[0] > config.x_border[0]) is True
    assert (x_y_List[0] < config.x_border[1]) is True
    assert (x_y_List[1] > config.y_border[0]) is True
    assert (x_y_List[1] < config.y_border[1]) is True

def test_max_ants():
    assert isinstance(config.max_ants, int) is True
    assert config.max_ants>0

def test_n():
    assert config.n == config.max_ants

def test_x_border():
    assert isinstance(config.x_border, list) is True
    assert len(config.x_border) == 2
    assert config.x_border[0] == 0
    assert config.y_border[1] > 0

def test_y_border():
    assert isinstance(config.y_border, list) is True
    assert len(config.y_border) == 2
    assert config.y_border[0] == 0
    assert config.y_border[1] > 0

def test_loglevel():
    assert config.log_level in config.level