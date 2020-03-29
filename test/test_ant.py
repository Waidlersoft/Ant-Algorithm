import syspath
from algorithm.ant import ant
from algorithm.common import common

def test_birth():
    assert ant.birth({},2) == {2: {"pos": common.startpoint,
                         "status": "search",
                         "pheromones": 200}}
    assert  ant.birth({1:{}},2) == {1:{},
                                    2: {"pos": common.startpoint,
                         "status": "search",
                         "pheromones": 200}}