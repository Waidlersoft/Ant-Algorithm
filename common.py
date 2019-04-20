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
