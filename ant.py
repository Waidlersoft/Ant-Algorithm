import random,matplotlib
import matplotlib.pyplot as plt
import numpy as np

direction = [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[1,-1],[0,-1]]
start = ["010010"]
target = ["090090"]
n = 1 #number of ants
x_border = [0,100]
y_border = [0,100]
            
def main():
    playgr = field.start()
    ants = ant.create()
    pos_list =[]
    for j in range(0,100000): 
        for i in range(0,n):
            smell_list = ant.smell(ants[i]["pos"],playgr)
            direction = ant.move(smell_list,ants[i]["status"])
            ant.pheromons(ants[i]["pos"],playgr,ants[i]["status"])
            antchange = ant.modechange(ants[i]["pos"],ants[i])
            ants.update(antchange)
            position = ant.position(ants,direction)
            pos_new = ants[i]["pos"]
            pos_list.append(pos_new)
    field.paint(pos_list)
    plt.show()

  
class common():
    def poskey(x,y):
        positionkey = (3-len(str(x)))*"0"+str(x*1000+y)
        return positionkey

    def xy_pos(pos):
        pos_x = int(pos[:3])
        pos_y = int(pos[4:6])
        return [pos_x,pos_y]
        
class ant():
    def create(ants={},n=1):
        ants = {}
        for i in range(0,n):
            ants.update({i:{"pos":"010010",
                            "status":"search"}
                         }
                        )
        return ants

    def move(value_list=[1,1,1,1,1,1,1,1],status="border"):
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

    def smell(pos,field):
        smell_list =[]
        x=int(pos[:3])
        y=int(pos[4:6])
        for i in direction:
            pos_x=x+i[0]
            pos_y=y+i[1]
            pos_key=common.poskey(pos_x,pos_y)
            smell_list.append(field[pos_key])
        return smell_list
    
    def position(ants,direction):
        for i in range(0,n):
            ant_value = ants[i]
            pos_old=ant_value["pos"]
            pos_x = int(pos_old[:3])
            pos_y = int(pos_old[4:6])
            pos_new = common.poskey(pos_x+direction[0],pos_y+direction[1])
            ant_value.update({"pos":pos_new})
            ants.update({i:ant_value})

    def pheromons(pos,field,mode):
        new_value=field[str(pos)][mode]+1
        cell=field[pos]
        cell.update({mode:new_value})
        field.update({pos:cell})
        return field

    def modechange(pos,a):
        stat = a["status"]
        if pos == target:
            stat = "return"
            
        elif pos == start:
            stat = "search"
        else:
            pass
        a.update({"status":stat})
        return a
        

class field():
    def start():
        field = {}
        for x in range(0,101):
            for y in range(0,101):
                keystring = common.poskey(x,y)
                if x in x_border or y in y_border:
                    n = 0
                else:
                    n = 1
                field.update({keystring:{"border":n,
                                         "search":n,
                                         "return":n
                                         }
                              }
                             )
        return field

    def paint(pos):
        x_list = []
        y_list = []
        for i in pos:
            pos_value = common.xy_pos(i)
            x_list.append(pos_value[0])
            y_list.append(pos_value[1])
        fig, ax = plt.subplots()
        ax.plot(x_list, y_list,'o')
main()
