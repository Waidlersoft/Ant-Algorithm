import matplotlib.pyplot as plt
from common import common
from log import log


class field():


    def start():
        field = {}
        for x in range(common.x_border[0],common.x_border[1]+1):
            for y in range(common.y_border[0],common.y_border[1]+1):
                keystring = common.poskey(x,y)
                if x in common.x_border or y in common.y_border:
                    n = 0
                else:
                    n = 1
                field.update({keystring:{"border":n,
                                         "search":n,
                                         "return":n}})
        return field

    def prepare():
        ax = plt.axes()
        plt.xlim(common.x_border[0],common.x_border[1]) 
        plt.ylim(common.y_border[0],common.y_border[1])
        POIx=[common.xy_pos(common.startpoint)[0],common.xy_pos(common.targetpoint)[0]]
        POIy=[common.xy_pos(common.startpoint)[1],common.xy_pos(common.targetpoint)[1]]
        ax.set_title("Ant algorithm")
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
        ax.scatter(xreturn, yreturn,facecolor='green')
        POIx=[common.xy_pos(common.startpoint)[0],common.xy_pos(common.targetpoint)[0]]
        POIy=[common.xy_pos(common.startpoint)[1],common.xy_pos(common.targetpoint)[1]]
        ax.scatter([POIx], [POIy],facecolor="blue")
        log.write("Collection before:"+str(ax.collections))
        plt.draw() 
        plt.pause(0.01)
        ax.lines[0].remove()
        for i in range(0,2):
            try:
                ax.collections[0].remove()
            except:
                break
        log.write("Collection after:"+str(ax.collections))
        ax.plot()
                
    def wind(field):
        for x in range(common.x_border[0],common.x_border[1]+1):
            for y in range(common.y_border[0],common.y_border[1]+1):
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
                field.update({keystring:{"border":field[keystring]["border"],
                                         "search":searchPheromones,
                                         "return":returnPheromones}})
        return field