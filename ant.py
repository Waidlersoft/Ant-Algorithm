import random

direction = [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[1,-1],[0,-1]]
start = ["010010"]
target = ["090090"]
x_border = [0,100]
y_border = [0,100]
            
def main():
    playgr = field.start()
    ant.create()
    smell = ant.smell()
    direction = ant.move(smell)
    print (str(direction))
    print (str(playgr))

class common():
    def poskey(x,y):
        positionkey = (3-len(str(x)))*"0"+str(x*1000+y)
        return positionkey
        
class ant():
    def create(ants={},n=1):
        for i in range(0,n+1):
            ants.update({i:
                            {"pos":"010010",
                            "status":"search"}
                         }
                        )
        return ants

    def move(value_list):
            n = random.random()
            j = 0
            grade = 0
            for i in value_list:
                j = j+1
                if i == 0:
                    continue
                else:
                    grade = grade + i/sum(value_list)
                    if n <= grade:
                        break
            return direction[j - 1]

    def smell(pos,field):
        smell =[]
        x=int(pos[:3])
        y=int(pos[4:6])
        for i in direction:
            pos_x=x+i[0]
            pos_y=y+i[1]
            pos_key=common.poskey(pos_x,pos_y)
            smell_list.append(field[pos_key])
        return smell_list

    def pheromons(pos,field,mode):
        new_value=field[pos][mode]+1
        cell=field[pos]
        cell.update(mode:new_value)
        field.update(pos:cell)
        return field

    def mode(pos):
        if pos == target:
            mode = "return"
        elif pos == start:
            mode = "search"
        else:
            pass
        return mode

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
main()
