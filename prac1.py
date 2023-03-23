def init():
    width = float(input())
    length = float(input())
    height = float(input())
    return width + length + height

def check() :
    checkval = init()
    if(checkval <= 80.0):
        return 5000
    elif(checkval <= 100):
        return 8000
    elif (checkval <= 120.0):
        return 10000
    elif (checkval <= 160.0):
        return 12000


print("Total Volume : ", check())
