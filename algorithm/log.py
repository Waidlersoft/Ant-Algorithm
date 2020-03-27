import datetime
import algorithm.config as config


class log():
    def create():
        with open ('log.txt','w') as f:
            f.write('Ant-algorithm log\n')

    def write(text,status='trace'):
        with open ('log.txt','a') as f:
            for i in config.level:
                if i == status:
                    pot = datetime.datetime.now().isoformat()[:19]
                    output = pot+" "+status+":"+str(text)+"\n"
                    print(output)
                    f.write(output)
                if i == config.log_level:
                    break
