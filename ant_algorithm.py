import matplotlib
import matplotlib.pyplot as plt
from ant import ant
from common import common
from field import field

direction = [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1]]
startpoint = "001001"
target = ["009009"]
n = 5 #number of ants

def main():
    ax = field.prepare(startpoint,target)
    playgr = field.start()
    ants = ant.create(n,startpoint)
    pos_list =[]
    j=0
    while 1:
        j = j+1
        pltlistsearch=[]
        pltlistreturn=[]
        for i in range(0,n):
            an = ants[i]
            smell_list = ant.smell(an["pos"],playgr,direction)
            direction_value = ant.move(smell_list,an["status"],direction)
            ant.pheromons(an["pos"],playgr,common.switchstatus(ants[i]["status"]),an,startpoint)
            antchange = ant.modechange(an["pos"],an,startpoint,target)
            ants.update(antchange)
            position = ant.position(i,ants,ants[i],direction_value)
            pos_new = an["pos"]
            if an["status"]=="search":
                pltlistsearch.append(pos_new)
            else:
                pltlistreturn.append(pos_new)
        field.wind(playgr)
        ant.printtext(j,i,an["status"], smell_list,pos_new)
        field.paint(pltlistsearch,pltlistreturn,plt,ax)

main()
