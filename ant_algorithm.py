import matplotlib
import matplotlib.pyplot as plt
from ant import ant
from common import common
from field import field
from log import log

def main():
    log.create()
    ax = field.prepare()
    playgr = field.start()
    ants = ant.create()
    log.write(ants,"trace")
    j=0
    while j<10000:
        j = j+1
        pltlistsearch=[]
        pltlistreturn=[]
        for i in range(0,common.n):
            an = ants[i]
            ant.modechange(ants,i)
            ant.position(i,ants,playgr)
            pos_new = an["pos"]
            if an["status"]=="search":
                pltlistsearch.append(pos_new)
            else:
                pltlistreturn.append(pos_new)
            log.write(ant.printtext(j,i,an["status"],pos_new))
        field.wind(playgr)
        field.paint(pltlistsearch,pltlistreturn,plt,ax)

main()
