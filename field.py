import matplotlib.pyplot as plt
from common import common

x_border = [0,10]
y_border = [0,10]

class field():
    def start():       
        field = {}
        for x in range(x_border[0],x_border[1]+1):
            for y in range(y_border[0],y_border[1]+1):
                keystring = common.poskey(x,y)
                if x in x_border or y in y_border:
                    n = 0
                else:
                    n = 1
                field.update({keystring:{"search":n,
                                         "return":n}})
        return field

    def prepare(start,target):
        ax = plt.axes()
        plt.xlim(0,10) 
        plt.ylim(0,10)
        POIx=[]
        POIy=[]
        POIx.append(common.xy_pos(start)[0])
        POIy.append(common.xy_pos(start)[1])
        POIx.append(common.xy_pos(target[0])[0])
        POIy.append(common.xy_pos(target[0])[1])
        ax.scatter([POIx], [POIy])
        return ax
   
    def paint(possearch,posreturn,plt,ax):
        xsearch=[]
        ysearch=[]
        xreturn=[]
        yreturn=[]
        for i in possearch:
            xsearch.append(common.xy_pos(i)[0])
            ysearch.append(common.xy_pos(i)[1])
        for i in posreturn:
            xreturn.append(common.xy_pos(i)[0])
            yreturn.append(common.xy_pos(i)[1])
        ax.plot(xsearch, ysearch, 'ro')
        plt.draw() 
        plt.pause(0.01)
        ax.lines[0].remove()
        
    def wind(field):
        for x in range(x_border[0],x_border[1]+1):
            for y in range(y_border[0],y_border[1]+1):
                keystring = common.poskey(x,y)
                pheromones = field[keystring]
                searchPheromones=100
                returnPheromones=100
                if pheromones["search"]>10:
                    searchPheromones= pheromones["search"]-1
                else:
                    searchPheromones= pheromones["search"]
                if pheromones["return"]>10:
                    returnPheromones= pheromones["return"]-1
                else:
                    eturnPheromones= pheromones["return"]
                field.update({keystring:{"search":searchPheromones,
                                         "return":returnPheromones}})
        return field
