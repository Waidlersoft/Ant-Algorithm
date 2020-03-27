from algorithm.log import log
import algorithm.config as config

class common():
    direction = config.direction
    startpoint = config.startpoint
    targetpoint = config.targetpoint
    max_ants = config.max_ants
    n = config.max_ants
    pos_list = config.pos_list
    x_border = config.x_border
    y_border = config.y_border

    def poskey(x,y):
        if not isinstance(y, int) or not isinstance(x, int):
            return False
        if (x>999) or (y>999):
            return False
        posNr = str(x*1000+y)
        positionkey = (6-len(posNr))*"0"+posNr
        log.write("x:"+str(x)+"y:"+str(y)+"="+positionkey)
        return positionkey

    def xy_pos(pos):
        if len(pos)==6:
            pos_x = int(pos[:3])
            pos_y = int(pos[4:6])
            return [pos_x,pos_y]
        else:
            return False

    def switchstatus(status):
        switch = {"search":"return",
         "return":"search"}
        return switch[status]