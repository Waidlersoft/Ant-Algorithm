import matplotlib
import matplotlib.pyplot as plt
from ant import ant
from common import common
from field import field

def main():
    ax = field.prepare()
    playgr = field.start()
    ants = ant.create()
    j=0
    while 1:
        j = j+1
        pltlistsearch=[]
        pltlistreturn=[]
        for i in range(0,common.n):
            an = ants[i]
            smell_list = ant.smell(an["pos"],playgr)
            direction_value = ant.move(smell_list,an["status"])
            ant.pheromons(playgr,ants,i)
            antchange = ant.modechange(an)
            ants.update(antchange)
            position = ant.position(i,ants,direction_value)
            pos_new = an["pos"]
            if an["status"]=="search":
                pltlistsearch.append(pos_new)
            else:
                pltlistreturn.append(pos_new)
        field.wind(playgr)
        ant.printtext(j,i,an["status"], smell_list,pos_new)
        field.paint(pltlistsearch,pltlistreturn,plt,ax)

main()
