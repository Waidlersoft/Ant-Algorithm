import algorithm.ant_algorithm, algorithm.config


def test_preparation():
    x_border = config.x_border
    y_border = config.y_border
    returnvalue = ant_algorithm.preparation()
    playground = returnvalue[1]
    ants = returnvalue[2]
    assert isinstance(returnvalue, tuple)
    assert isinstance(playground, dict)
    assert isinstance(ants, dict)
    assert len(playground) == (x_border[1]-x_border[0]+1)*(y_border[1]-y_border[0]+1)
    assert len(ants) == config.max_ants

def test_ant_changing():
    assert ant_algorithm.ants_changing(1, {}, {}) == False