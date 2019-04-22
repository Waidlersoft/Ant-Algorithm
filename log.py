import datetime
class log():
    def write(f,text,status):
        pot = datetime.datetime.now().isoformat()[:19]
        output= pot+" "+status+":"+str(text)
        if status == "info":
            print(output)
            f.write(output)
