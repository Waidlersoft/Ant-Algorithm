from common import common
import random

class ant():
        def create(n=1,start="001001"):
                ants = {}
                for i in range(0,n):
                    ants.update({i:{"pos":start,
                                    "status":"search",
                                    "pheromones":200}})
                return ants

        def move(value_list,status,direction):
                    rnd = random.random()
                    j = 0
                    grade = 0
                    val_sum = 0
                    for i in value_list:
                        val_sum = val_sum + int(i[status])
                    for i in value_list:
                        j = j+1
                        if i[status] == 0:
                            continue
                        else:
                            grade = grade + i[status]/val_sum
                            if rnd <= grade:
                                break
                    return direction[j - 1]

        def smell(pos,field,direction):
                smell_list =[]
                x=int(pos[:3])
                y=int(pos[4:6])
                for i in direction:
                    pos_x=x+i[0]
                    pos_y=y+i[1]
                    pos_key=common.poskey(pos_x,pos_y)
                    smell_list.append(field[pos_key])
                return smell_list
            
        def position(i,ants,ant_value,direction):
                pos_old=ant_value["pos"]
                pos_x = int(pos_old[:3])
                pos_y = int(pos_old[4:6])
                pos_new = common.poskey(pos_x+direction[0],pos_y+direction[1])
                ant_value.update({"pos":pos_new})
                ants.update({i:ant_value})

        def pheromons(pos,field,mode,ant,start="001001"):
                new_value=field[str(pos)][mode]+ant["pheromones"]
                cell=field[pos]
                cell.update({mode:new_value})
                field.update({pos:cell})
                if ant["pheromones"]>1:
                        ant.update({"pheromones":ant["pheromones"]-1})
                else:
                        ant.update({"pos":start,
                                    "status":"search",
                                    "pheromones":200})
                return field

        def modechange(pos,a,start,target):
                stat = a["status"]
                if pos == target:
                    stat = "return"
                elif pos == start:
                    stat = "search"
                else:
                    pass
                a.update({"status":stat})
                return a
                
        def printtext(roundnr,antnr,status, value_list,position):
                text =str(roundnr)+"Ant"+str(antnr)+":"+str(status)+"-- search:"
                for i in value_list:
                    text=text+str(i["search"])+","
                text = text + "-- return:"
                for i in value_list:
                    text=text+str(i["return"])+","
                text = text+" Pos:"+str(position)
                print(text)
