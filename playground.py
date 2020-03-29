import algorithm.ant_algorithm as algo
from algorithm.log import log

def main():
    dictionary = log.create()
    print(type(dictionary.__getattribute__('name')))

if __name__ == '__main__':
    main()