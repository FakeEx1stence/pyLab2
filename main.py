import math

def main():
    while True:
        print(" Choose task: "
              "\n1. Task 1\n2.Task2\n3.Task3\n4.Close")
        ch = int(input("Enter task "))

        if ch == 1: print(task1())
        elif ch == 2: print(task2())
        elif ch == 3: print(task3())
        elif ch == 4: exit()

def task1():
    class Dot:
        x = 0
        y = 0

    a = Dot()
    print(" A.x = ")
    a.x = int(input())
    print(" A.y = ")
    a.y = int(input())

    b = Dot()
    print(" B.x = ")
    b.x = int(input())
    print(" B.y = ")
    b.y = int(input())

    c = Dot()
    print(" C.x = ")
    c.x = int(input())
    print(" C.y = ")
    c.y = int(input())

    d = Dot()
    if (a.x == b.x or a.x == c.x or b.x == c.x) and (a.y == b.y or a.y == c.y or b.y == c.y):
        if a.x == c.x:
            d.x = b.x
        elif a.x == b.x:
            d.x = c.x
        else:
            d.x = a.x

        if a.y == b.y:
            d.y = c.y
        elif a.y == c.y:
            d.y = b.y
        else:
            d.y = a.y

        return (d.x, d.y)
    else:
        return ("Неправильні координати прямокутника відносно осей")


def task2():
    try:
        x = float(input())
        y = float(input())
        r = float(input())

        if (x < 0 and y < 0 and pow((x+r), 2) + pow((y+r), 2) < pow(r, 2) and y < -x-2*r and x < -r):
            return("In")
        elif (x > 0 and 0 < y < -y + 2 * r and x > r and x < 2*r and pow((x - r), 2) + pow((y - r), 2) > pow(r, 2) and x < -y+2*r):
            return("In")
        else:
            return("Out")
    except:
        print("Помилка")
        return 0

def task3():
    try:
        n = 1
        e = pow(10, 5)
        g = pow(10, -5)
        result = 0

        while result < e:
            result += pow(5, n)/(math.sqrt(n)*pow(2, (n-1)))
            print("Result is ")
            print(result)
            n += 1


        return result
    except:
        print("Помилка")
        return 0





main()
