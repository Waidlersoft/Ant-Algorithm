import algorithm.ant_algorithm as algo
from algorithm.log import log

def main():
    ax,playgr,ants = algo.preparation()
    axDict = ax.__dict__
    subplot = axDict['figure'].__dict__
    subplot = subplot['canvas'].__dict__
    subplot = subplot['figure'].__dict__
    subplot = axDict
    for item in subplot:
        print(str(item)+":"+str(subplot[item]))
    #    log.write((str(item)+":"+str(axDict[item])),"warn")

if __name__ == '__main__':
    main()