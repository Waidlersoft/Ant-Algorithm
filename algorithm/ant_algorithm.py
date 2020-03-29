import matplotlib.pyplot as plt
from algorithm.ant import ant
import algorithm.config as config
from algorithm.fieldpreparation import FieldPreparation
from algorithm.log import log

def preparation():
    log.create()
    ax = FieldPreparation.prepare()
    playgr = FieldPreparation.create_field()
    ants = ant.create()
    log.write(ants,"trace")
    return (ax,playgr,ants)

def ants_changing(j, ants, playground):
    pltlistsearch = []
    pltlistreturn = []
    for i in range(0, config.max_ants):
        try:
            an = ants[i]
        except:
            return False
        ant.modechange(ants, i)
        ant.position(i, ants, playground)
        pos_new = an["pos"]
        if an["status"] == "search":
            pltlistsearch.append(pos_new)
        else:
            pltlistreturn.append(pos_new)
        log.write(ant.printtext(j, i, an["status"], pos_new))
    return pltlistsearch, pltlistreturn

def start():
    ax, playground, ants = preparation()
    for j in range(1, 10):
        pltlistsearch, pltlistreturn = ants_changing(j, ants, playground)
        FieldPreparation.wind(playground)
        FieldPreparation.paint(pltlistsearch, pltlistreturn, plt, ax)
    return True


if __name__ == "__main__":
    start()
