from common import common
from log import log
import random

class ant():
        def birth(ants,i):
                ants.update({i:{"pos":common.startpoint,
                                "status":"search",
                                "pheromones":200}})
                return ants
        
        def create(n=1):
                ants = {}
                for i in range(0,common.n):
                    ants=ant.birth(ants,i)
                return ants

        def move(i,ants, field):
                value_list=ant.smell(ants[i]["pos"],field)
                status = ants[i]["status"]
                rnd = random.random()
                j = 0
                grade = 0
                val_sum = 0
                for n in value_list:
                        val_sum = val_sum + int(n[status])
                for n in value_list:
                        j = j+1
                        if n[status] == 0:
                                continue
                        else:
                                grade = grade + n[status]/val_sum
                                if rnd <= grade:
                                        break
                return common.direction[j - 1]

        def smell(pos,field):
                smell_list =[]
                x=int(pos[:3])
                y=int(pos[4:6])
                log.write("Smelling field:"+str(field)) 
                for i in common.direction:
                    pos_x=x+i[0]
                    pos_y=y+i[1]
                    pos_key=common.poskey(pos_x,pos_y)
                    fieldPos = field[pos_key]
                    log.write("Smell:"+str(pos_key)+"field:"+str(fieldPos))
                    border = fieldPos["border"]
                    smell_list.append({"border":border,
                                       "search":fieldPos["search"]*border,
                                       "return":fieldPos["return"]*border})
                log.write(smell_list,'trace')
                return smell_list
            
        def position(i,ants,field):
                direct=ant.move(i,ants,field)
                pos_old=ants[i]["pos"]
                pos_x = int(pos_old[:3])
                pos_y = int(pos_old[4:6])
                pos_new = common.poskey(pos_x+direct[0],pos_y+direct[1])
                ants[i].update({"pos":pos_new})
                ants.update({i:ants[i]})
                text = "pos_old:"+pos_old+"--direct:"+str(direct)+"pos_new:"+pos_new
                log.write(text,"trace")

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

        def modechange(ants,i):
                stat = ants[i]["status"]
                pos = ants[i]["pos"]
                an = ants[i]
                if pos == common.targetpoint:
                    stat = "return"
                elif pos == common.startpoint:
                    stat = "search"
                else:
                    pass
                an.update({"status":stat})
                ants.update({i:an})
                
        def printtext(roundnr,antnr,status,position):
                text =str(roundnr)+"Ant"+str(antnr)+":"+str(status)+"--Pos:"+str(position)
                return text