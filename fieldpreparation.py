import matplotlib.pyplot as plt
from common import common
from log import log


class FieldPreparation:
    def create_field(self=""):
        playing_field = {}
        for x in range(common.x_border[0], common.x_border[1] + 1):
            for y in range(common.y_border[0], common.y_border[1] + 1):
                key_string = common.poskey(x, y)
                n = 1
                if x in common.x_border or y in common.y_border:
                    n = 0
                playing_field.update({key_string: {"border": n,
                                                  "search": n,
                                                  "return": n}})
        return playing_field

    def prepare(self=""):
        ax = plt.axes()
        plt.xlim(common.x_border[0], common.x_border[1])
        plt.ylim(common.y_border[0], common.y_border[1])
        poi_x = [common.xy_pos(common.startpoint)[0], common.xy_pos(common.targetpoint)[0]]
        poi_y = [common.xy_pos(common.startpoint)[1], common.xy_pos(common.targetpoint)[1]]
        ax.set_title("Ant algorithm")
        ax.scatter([poi_x], [poi_y])
        return ax

        xsearch = []
        ysearch = []
        xreturn = []
        yreturn = []
        for i in possearch:
            xsearch.append(common.xy_pos(i)[0])
            ysearch.append(common.xy_pos(i)[1])
        for i in posreturn:
            xreturn.append(common.xy_pos(i)[0])
            yreturn.append(common.xy_pos(i)[1])
        ax.plot(xsearch, ysearch, 'ro')
        ax.scatter(xreturn, yreturn, facecolor='green')
        POIx = [common.xy_pos(common.startpoint)[0], common.xy_pos(common.targetpoint)[0]]
        POIy = [common.xy_pos(common.startpoint)[1], common.xy_pos(common.targetpoint)[1]]
        ax.scatter([POIx], [POIy], facecolor="blue")
        log.write("Collection before:" + str(ax.collections))
        plt.draw()
        plt.pause(0.01)
        ax.lines[0].remove()
        for i in range(0, 2):
            try:
                ax.collections[0].remove()
            except:
                break
        log.write("Collection after:" + str(ax.collections))
        ax.plot()

    def wind(field_dictionary={}):
        for x in range(common.x_border[0], common.x_border[1] + 1):
            for y in range(common.y_border[0], common.y_border[1] + 1):
                key_string = common.poskey(x, y)
                try:
                    pheromones = field_dictionary[key_string]
                except:
                    return False
                search_pheromones = 10
                return_pheromones = 10
                if pheromones["search"] > 10:
                    search_pheromones = pheromones["search"] - 1
                else:
                    search_pheromones = pheromones["search"]
                if pheromones["return"] > 10:
                    return_pheromones = pheromones["return"] - 1
                else:
                    return_pheromones = pheromones["return"]
                field_dictionary.update({key_string: {"border": field_dictionary[key_string]["border"],
                                                      "search": search_pheromones,
                                                      "return": return_pheromones}})
        return field_dictionary
