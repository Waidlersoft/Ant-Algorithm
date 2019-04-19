import random,matplotlib
import matplotlib.pyplot as plt
import numpy as np

direction = [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[1,-1],[0,-1]]
start = ["010010"]
target = ["090090"]
n = 1 #number of ants
x_border = [0,100]
y_border = [0,100]
statuslist = ["search","return"]

def main():
    ax = plt.axes()
    plt.xlim(0,100) 
    plt.ylim(0,100)
    playgr = field.start()
    ants = ant.create()
    pos_list =[]
    for j in range(0,100000): 
        for i in range(0,n):
            smell_list = ant.smell(ants[i]["pos"],playgr)
            direction = ant.move(smell_list,ants[i]["status"])
            ant.pheromons(ants[i]["pos"],playgr,common.switchstatus(ants[i]["status"]))
            antchange = ant.modechange(ants[i]["pos"],ants[i])
            ants.update(antchange)
            position = ant.position(ants,direction)
            pos_new = ants[i]["pos"]
            field.paint(pos_new,ax)
  
class common():
    def poskey(x,y):
        positionkey = (3-len(str(x)))*"0"+str(x*1000+y)
        return positionkey

    def xy_pos(pos):
        pos_x = int(pos[:3])
        pos_y = int(pos[4:6])
        return [pos_x,pos_y]

    def switchstatus(status):
        if status == "search":
            i = "return"
        else: i = "return"
        return i
        
class ant():
    def create(ants={},n=1):
        ants = {}
        for i in range(0,n):
            ants.update({i:{"pos":"010010",
                            "status":"search"}
                         }
                        )
        return ants

    def move(value_list=[1,1,1,1,1,1,1,1],status="search"):
            rnd = random.random()
            j = 0
            grade = 0
            val_sum = 0
            text =str(status)+"-- search:"
            for i in value_list:
                text=text+str(i["search"])+","
            text = text + "-- return:"
            for i in value_list:
                text=text+str(i["return"])+","
            print(text)
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
                field.update({keystring:{"search":n,
                                         "return":n
                                         }
                              }
                             )
        return field

    def paint(pos,ax):       
            x= common.xy_pos(pos)[0]
            y= common.xy_pos(pos)[1]
            ax.plot([x], [y], 'ro')
            plt.draw() 
            plt.pause(0.01)
            ax.lines[0].remove()

main()
