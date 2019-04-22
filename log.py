import datetime
class log():
    Level = ["Info","Log","Debug"]
    Loglevel = "Log"
    def create():
        with ('log.txt','w') Open as f:
           f.write('Ant-algorithm log')

    def write(f,text,status):
        with ('log.txt','a') Open as f:
         For i in Level:
          If i == Status:
            pot = datetime.datetime.now().isoformat()[:19]
            output= pot+" "+status+":"+str(text)
            print(output)
            f.write(output)
          If i==loglevel:
               break
