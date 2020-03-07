import matplotlib
import matplotlib.pyplot as plt
from ant import ant
from common import common
from field import field
from log import log

def preparation():
    log.create()
    ax = field.prepare()
    playgr = field.start()
    ants = ant.create()
    log.write(ants,"trace")
    return (ax,playgr,ants)
    
def main():
    ax,playgr,ants = preparation()
    for j in range(1,10000):
        pltlistsearch=[]
        pltlistreturn=[]
        for i in range(0,common.max_ants):
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

if __name__ == "__main__":
    main()