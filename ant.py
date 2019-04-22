from common import common
import random

class ant():
        def birth(ants,i):
                ants.update({i:{"pos":common.startpoint,
                                "status":"search",
                                "pheromones":200}})
                return ants
        def create(n=1):
                ants = {}
                for i in range(0,n):
                    ants=ant.birth(ants,i)
                return ants

        def move(value_list,status):
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
                    return common.direction[j - 1]

        def smell(pos,field):
                smell_list =[]
                x=int(pos[:3])
                y=int(pos[4:6])
                for i in common.direction:
                    pos_x=x+i[0]
                    pos_y=y+i[1]
                    pos_key=common.poskey(pos_x,pos_y)
                    smell_list.append(field[pos_key])
                return smell_list
            
        def position(i,ants,direct):
                pos_old=ants[i]["pos"]
                pos_x = int(pos_old[:3])
                pos_y = int(pos_old[4:6])
                pos_new = common.poskey(pos_x+direct[0],pos_y+direct[1])
                ants[i].update({"pos":pos_new})
                ants.update({i:ants[i]})

        def pheromons(field,ants,i):
                an = ants[i]
                pos=an["pos"]
                mode = common.switchstatus(an["status"])
                new_value=field[str(pos)][mode]+an["pheromones"]
                cell=field[pos]
                cell.update({mode:new_value})
                field.update({pos:cell})
                if an["pheromones"]>1:
                        an.update({"pheromones":an["pheromones"]-1})
                else:
                        ant.birth(ants,i)
                return field

        def modechange(an):
                stat = an["status"]
                if an["pos"] == common.targetpoint:
                    stat = "return"
                elif an["pos"] == common.startpoint:
                    stat = "search"
                else:
                    pass
                an.update({"status":stat})
                return an
                
        def printtext(roundnr,antnr,status, value_list,position):
                text =str(roundnr)+"Ant"+str(antnr)+":"+str(status)+"-- search:"
                for i in value_list:
                    text=text+str(i["search"])+","
                text = text + "-- return:"
                for i in value_list:
                    text=text+str(i["return"])+","
                text = text+" Pos:"+str(position)
                print(text)
