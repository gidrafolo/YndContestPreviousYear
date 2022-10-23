import sys


def main():
    dict_seats = {0: 'A', 1: 'B', 2: 'C', 4: 'D', 5: 'E', 6: 'F'} # словарь навзаний сидений
    # вводим изначальную рассадку
    airplane_plan = []
    n = int(input())
    for i in range(n):
        ryad = [x for x in input()]
        airplane_plan.append(ryad)
    # вывод рассадки для проверки работоспособности
    # for i in airplane_plan:
    #     print(i)
    ## заполняем места новыми пассажирами
    q = int(input())
    for i in range(q):
        WhatPassWant = input().split()
        set_newpass(WhatPassWant[0], WhatPassWant[1], WhatPassWant[2], airplane_plan)
        renameX_print(airplane_plan, dict_seats)


def renameX_print(airplane_plan, dict_seats):
    Xseats = 'Passengers can take seats:'
    i = 1
    # выясняем как называются места которые заняли новые пассажиры
    for line in airplane_plan:
        for j in range(len(line)):
            if line[j] == 'X':
                Xseats += (' '+f'{i}'+dict_seats[j])
        i += 1
    # выводим ответ
    if Xseats == 'Passengers can take seats:':
        print('Cannot fulfill passengers requirements')
    else:
        print(Xseats)
        for line in airplane_plan:
            for x in line:
                print(x, end = '')
            print()
    # заменяем Х на #
    for line in airplane_plan:
        for j in range(len(line)):
            if line[j] == 'X':
                line[j] = '#'

def set_newpass(count, side, part, airplane_plan):
    i = 0
    for line in airplane_plan:
        if side == 'left':
            if count == '3':
                if line[0] == '.' and line[1] == '.' and line[2] == '.':
                    line[0],line[1],line[2] = 'X','X','X'
                    break
            if part == 'aisle':
                if count == '2':
                    if line[1] == '.' and line[2] == '.':
                        line[1], line[2] = 'X','X'
                        break
                if count == '1':
                    if line[2] == '.':
                        line[2] = 'X'
                        break
            if part == 'window':
                if count == '2':
                    if line[0] == '.' and line[1] == '.':
                        line[0], line[1] = 'X','X'
                        break
                if count == '1':
                    if line[0] == '.':
                        line[0] = 'X'
                        break
        if side == 'right':
            if count == '3':
                if line[4] == '.' and line[5] == '.' and line[6] == '.':
                    line[4],line[5],line[6] = 'X','X','X'
                    break
            if part == 'aisle':
                if count == '2':
                    if line[4] == '.' and line[5] == '.':
                        line[4], line[5] = 'X','X'
                        break
                if count == '1':
                    if line[4] == '.':
                        line[4] = 'X'
                        break
            if part == 'window':
                if count == '2':
                    if line[5] == '.' and line[6] == '.':
                        line[5], line[6] = 'X','X'
                        break
                if count == '1':
                    if line[6] == '.':
                        line[6] = 'X'
                        break

if __name__ == "__main__":
    main()