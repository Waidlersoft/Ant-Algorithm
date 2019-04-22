import datetime
class log():
    Level = ["Info","Log","Debug"]
    def create():
        with ('log.txt','w') Open as f:
           f.write('Ant-algorithm log')

    def write(f,text,status):
        with ('log.txt','a') Open as f:
         pot = datetime.datetime.now().isoformat()[:19]
         output= pot+" "+status+":"+str(text)
         for i in Level:
             print(output)
             f.write(output)
             If i==Status:
               break
