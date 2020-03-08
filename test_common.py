from common import common

def test_birth():
    assert common.switchstatus("search") == "return"
    assert common.switchstatus("return") == "search"

def test_xy_pos():
    assert common.xy_pos("001002") == [1,2]
    assert common.xy_pos("00100") == False