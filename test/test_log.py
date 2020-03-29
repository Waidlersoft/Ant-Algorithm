import syspath
from algorithm.log import log
import algorithm.config as config

def test_create():
    logFileDictionay = log.create()
    assert logFileDictionay.__getattribute__('name') is config.logfile_name

def test_write():
    logFileDictionay = log.write("","fatal")
    assert logFileDictionay.__getattribute__('name') is config.logfile_name
