from algorithm.common import common

def test_birth():
    assert common.switchstatus("search") == "return"
    assert common.switchstatus("return") == "search"

def test_xy_pos():
    assert common.xy_pos("001002") == [1,2]
    assert common.xy_pos("00100") == False

def test_poskey():
    assert common.poskey(1,1) == "001001"
    assert common.poskey(999, 999) == "999999"
    assert common.poskey(9999, 9999) == False
    assert common.poskey("a", 9) == False
    assert common.poskey(9, "a") == False
    assert common.poskey(9, 1.1) == False