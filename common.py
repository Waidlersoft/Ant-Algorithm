from log import log

class common():
    direction = [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1]]
    startpoint = "001001"
    targetpoint = "009009"
    n = 50 #number of ants
    pos_list =[]
    x_border = [0,11]
    y_border = [0,11]

    def poskey(x,y):
        posNr = str(x*1000+y)
        positionkey = (6-len(posNr))*"0"+posNr
        log.write("x:"+str(x)+"y:"+str(y)+"="+positionkey)
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
