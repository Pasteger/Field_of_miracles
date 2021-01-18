from random import randint
import time
import turtle


Words = (
    'жупа',
    'буревестник',
    'испания',
    'подорожник',
    'инфляция',
    'валинор',
    'хамон',
    'утилиты'
)
# слова не должны быть длиннее 12 символов
Questions = (
    'Как у западных и южных славян назывались селение, деревня, курень?',
    'Старинное название барометра',
    'По одной из версий, название этой страны с одного из древних языков можно перевести как берег кроликов',
    'Какая трава была названа индейцами «следом белого человека»',
    'Этот термин произошел от латинского слова, переводимого на русский как «вздутие»',
    'Королевство правителей Арды в книгах английского писателя Дж. Толкина',
    'Испанский национальный деликатес',
    'Вспомогательные компьютерные программы в составе общего ПО'
)
Drum = (
    0, 1000, 500, 350, 550, 750, 600, 500, 350, 400, 'x2', 600, 500, 'n', 600, 350, 300, 200, 500, 600, 400, 'm', 500,
    350, 600, 400, 450, 500, 350, 600, '+', 400, 700, 600, 'x2', 600, 500, 400, 650, 450
)
Letter = [
    'ё', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д',
    'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'
]
Present = (
    'Средство от гемороя "Relief"', 'Билет в Геленджик в один конец', 'Купон в кафе У Артурчика на 100000 рублей',
    'Дакимакура с Джотаро Куджо', 'Бесплатный билет на курсы украинского языка', 'Роль в новом выпуске Гачимучи',
    'Пятиметровый портрет Сталина', 'Подарочная лицензия Minecraft', 'Колекция видеокоссет с выпусками Поля чудес'
)
coordinates = (-305, -265, -225, -185, -145, -105, -65, -25, 15, 55, 95, 135, 175)


# Функции барабана: начало
def free():
    turtle.left(180)
    turtle.forward(15)


def nol_():
    turtle.up()
    turtle.goto(310, 50)
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(10)
    turtle.up()
    turtle.goto(0, 0)


def nol():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(10)
    turtle.up()


def three():
    turtle.down()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.up()


def six_():
    turtle.down()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.up()


def five_():
    turtle.down()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.up()


def tis():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    nol()
    free()
    nol()
    free()
    turtle.setheading(90)
    turtle.down()
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def five():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    nol()
    free()
    five_()
    turtle.up()
    turtle.goto(0, 0)


def tri_five():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    five_()
    turtle.setheading(180)
    turtle.forward(15)
    turtle.setheading(270)
    turtle.forward(15)
    three()
    turtle.up()
    turtle.goto(0, 0)


def five_five():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    five_()
    turtle.setheading(180)
    turtle.forward(15)
    turtle.setheading(270)
    turtle.forward(15)
    five_()
    turtle.goto(0, 0)


def sem_five():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    five_()
    turtle.setheading(180)
    turtle.forward(15)
    turtle.setheading(270)
    turtle.forward(15)

    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(7)
    turtle.left(90)
    turtle.forward(2)
    turtle.up()
    turtle.goto(0, 0)


def six():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    nol()
    free()
    six_()
    turtle.goto(0, 0)


def four():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    nol()
    free()
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.up()
    turtle.goto(0, 0)


def x2():
    turtle.up()
    turtle.goto(310, 50)
    turtle.setheading(180)
    turtle.down()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(10)

    turtle.up()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.setheading(270)
    turtle.forward(15)
    turtle.down()

    turtle.setheading(135)
    turtle.forward(19)
    turtle.up()
    turtle.setheading(270)
    turtle.forward(14)
    turtle.down()
    turtle.setheading(0)
    turtle.left(45)
    turtle.forward(19)

    turtle.up()
    turtle.goto(0, 0)


def ban():
    turtle.up()
    turtle.goto(310, 50)
    six_()
    turtle.up()
    turtle.goto(0, 0)


def tri():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    nol()
    turtle.up()
    turtle.setheading(180)
    turtle.forward(15)
    turtle.down()

    turtle.setheading(180)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)

    turtle.up()
    turtle.goto(0, 0)


def dva():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    nol()
    free()
    turtle.down()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(10)

    turtle.up()
    turtle.goto(0, 0)


def present():
    turtle.up()
    turtle.goto(310, 50)
    turtle.setheading(90)
    turtle.down()
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def four_five():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    five_()
    turtle.up()
    turtle.setheading(180)
    turtle.forward(15)
    turtle.setheading(270)
    turtle.forward(15)
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.up()
    turtle.goto(0, 0)


def plus():
    turtle.up()
    turtle.goto(310, 50)
    turtle.setheading(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.down()
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(180)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def sem():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    nol()
    free()
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(7)
    turtle.left(90)
    turtle.forward(2)
    turtle.up()
    turtle.goto(0, 0)


def six_five():
    turtle.up()
    turtle.goto(310, 50)
    nol()
    free()
    five_()
    turtle.setheading(180)
    turtle.forward(15)
    turtle.setheading(270)
    turtle.forward(15)
    turtle.down()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.up()
    turtle.goto(0, 0)


def st_all():
    turtle.up()
    turtle.goto(310, 50)
    turtle.color('white')
    turtle.setheading(90)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(60)
    turtle.end_fill()
    turtle.up()
    turtle.color('black')
    turtle.goto(0, 0)


def squares():
    turtle.down()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.up()


def drum():
    input()
    st_all()
    for circle in range(5):
        rand = randint(0, len(Drum)-1)
        if rand == 0:
            nol_()
            st_all()
        elif rand == 1:
            tis()
            st_all()
        elif rand == 2:
            five()
            st_all()
        elif rand == 3:
            tri_five()
            st_all()
        elif rand == 4:
            five_five()
            st_all()
        elif rand == 5:
            sem_five()
            st_all()
        elif rand == 6:
            six()
            st_all()
        elif rand == 7:
            five()
            st_all()
        elif rand == 8:
            tri_five()
            st_all()
        elif rand == 9:
            four()
            st_all()
        elif rand == 10:
            x2()
            st_all()
        elif rand == 11:
            six()
            st_all()
        elif rand == 12:
            five()
            st_all()
        elif rand == 13:
            present()
            st_all()
        elif rand == 14:
            six()
            st_all()
        elif rand == 15:
            tri_five()
            st_all()
        elif rand == 16:
            tri()
            st_all()
        elif rand == 17:
            dva()
            st_all()
        elif rand == 18:
            five()
            st_all()
        elif rand == 19:
            six()
            st_all()
        elif rand == 20:
            four()
            st_all()
        elif rand == 21:
            ban()
            st_all()
        elif rand == 22:
            five()
            st_all()
        elif rand == 23:
            tri_five()
            st_all()
        elif rand == 24:
            six()
            st_all()
        elif rand == 25:
            four()
            st_all()
        elif rand == 26:
            four_five()
            st_all()
        elif rand == 27:
            five()
            st_all()
        elif rand == 28:
            tri_five()
            st_all()
        elif rand == 29:
            six()
            st_all()
        elif rand == 30:
            plus()
            st_all()
        elif rand == 31:
            four()
            st_all()
        elif rand == 32:
            sem()
            st_all()
        elif rand == 33:
            six()
            st_all()
        elif rand == 34:
            x2()
            st_all()
        elif rand == 35:
            six()
            st_all()
        elif rand == 36:
            five()
            st_all()
        elif rand == 37:
            four()
            st_all()
        elif rand == 38:
            six_five()
            st_all()
        elif rand == 39:
            four_five()
            st_all()

    rand = randint(0, len(Drum)-1)
    if rand == 0:
        nol_()
    elif rand == 1:
        tis()
    elif rand == 2:
        five()
    elif rand == 3:
        tri_five()
    elif rand == 4:
        five_five()
    elif rand == 5:
        sem_five()
    elif rand == 6:
        six()
    elif rand == 7:
        five()
    elif rand == 8:
        tri_five()
    elif rand == 9:
        four()
    elif rand == 10:
        x2()
    elif rand == 11:
        six()
    elif rand == 12:
        five()
    elif rand == 13:
        present()
    elif rand == 14:
        six()
    elif rand == 15:
        tri_five()
    elif rand == 16:
        tri()
    elif rand == 17:
        dva()
    elif rand == 18:
        five()
    elif rand == 19:
        six()
    elif rand == 20:
        four()
    elif rand == 21:
        ban()
    elif rand == 22:
        five()
    elif rand == 23:
        tri_five()
    elif rand == 24:
        six()
    elif rand == 25:
        four()
    elif rand == 26:
        four_five()
    elif rand == 27:
        five()
    elif rand == 28:
        tri_five()
    elif rand == 29:
        six()
    elif rand == 30:
        plus()
    elif rand == 31:
        four()
    elif rand == 32:
        sem()
    elif rand == 33:
        six()
    elif rand == 34:
        x2()
    elif rand == 35:
        six()
    elif rand == 36:
        five()
    elif rand == 37:
        four()
    elif rand == 38:
        six_five()
    elif rand == 39:
        four_five()

    if rand == 10 or rand == 34:
        print('Сектор x2 на барабане!')
        Points[number] *= 2
        print('Ваши очки умножены на 2')
    elif rand == 13:
        print('Сектор приз на барабане!')
        time.sleep(2)
        print('Возьмёте приз или 100 очков? (1 или 0)')
        v = input()
        if v == '1':
            print('Вы уверены? Может лучше возьмёте 1000 очков?')
            v = input()
            if v == '1':
                print('Да? Может лучше 1500 очков?')
                v = input()
                if v == '1':
                    v = randint(0, len(Presents))
                    print('Вы получаете', Present[v])
                    Presents[number].append(Present[v])
                else:
                    print('Вы выбрали очки')
                    Points[number] += 1500
            else:
                print('Вы выбрали очки')
                Points[number] += 1000
        else:
            print('Вы выбрали очки')
            Points[number] += 100
    elif rand == 21:
        print('Вы банкрот')
        Points[number] = 0
    elif rand == 30:
        print('Сектор плюс на барабане!')
        pass
    else:
        print('На баране', Drum[rand])
        Points[number] += Drum[rand]
        time.sleep(2)
    print('У вас', Points[number], 'очков')
# Функции барабана: конец


# Функции букв: начало
def o():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(20)
    turtle.up()


def a():
    turtle.down()
    turtle.setheading(112.5)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(10)
    turtle.right(70)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def b():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def bbb():
    turtle.down()
    turtle.setheading(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()


def g():
    turtle.setheading(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.down()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def d():
    turtle.setheading(90)
    turtle.down()
    turtle.forward(7)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(7)
    turtle.left(180)
    turtle.forward(7)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.up()
    turtle.goto(0, 0)


def e():
    turtle.setheading(180)
    turtle.forward(15)
    turtle.down()
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def iii():
    turtle.setheading(90)
    turtle.down()
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(42)
    turtle.right(135)
    turtle.forward(30)
    turtle.up()
    turtle.goto(0, 0)


def k():
    turtle.setheading(135)
    turtle.down()
    turtle.forward(22)
    turtle.left(135)
    turtle.forward(17)
    turtle.left(180)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(135)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def ll():
    turtle.down()
    turtle.setheading(112.5)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(30)
    turtle.up()
    turtle.goto(0, 0)


def m():
    turtle.down()
    turtle.setheading(100)
    turtle.forward(26)
    turtle.left(150)
    turtle.forward(26)
    turtle.setheading(100)
    turtle.forward(26)
    turtle.left(150)
    turtle.forward(26)
    turtle.up()
    turtle.goto(0, 0)


def j():
    turtle.down()
    turtle.setheading(135)
    turtle.forward(20)
    turtle.setheading(45)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(20)
    turtle.setheading(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(10)
    turtle.setheading(135)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(20)
    turtle.setheading(225)
    turtle.forward(20)
    turtle.up()
    turtle.goto(0, 0)


def n():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(30)
    turtle.up()
    turtle.goto(0, 0)


def p():
    turtle.setheading(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.down()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(30)
    turtle.up()
    turtle.goto(0, 0)


def r():
    turtle.setheading(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.down()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def s():
    turtle.setheading(180)
    turtle.forward(10)
    turtle.down()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(20)
    turtle.up()
    turtle.goto(0, 0)


def t():
    turtle.setheading(180)
    turtle.forward(15)
    turtle.down()
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(20)
    turtle.up()
    turtle.goto(0, 0)


def u():
    turtle.setheading(180)
    turtle.forward(30)
    turtle.setheading(45)
    turtle.down()
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def f():
    turtle.setheading(180)
    turtle.forward(15)
    turtle.down()
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.up()
    turtle.goto(0, 0)


def h():
    turtle.down()
    turtle.setheading(135)
    turtle.forward(19)
    turtle.up()
    turtle.setheading(270)
    turtle.forward(14)
    turtle.down()
    turtle.setheading(0)
    turtle.left(45)
    turtle.forward(19)
    turtle.up()
    turtle.goto(0, 0)


def c():
    turtle.setheading(90)
    turtle.down()
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(25)
    turtle.up()
    turtle.goto(0, 0)


def ch():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def sh():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(7)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(7)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def sch():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(12)
    turtle.right(90)
    turtle.forward(7)
    turtle.right(90)
    turtle.forward(12)
    turtle.right(180)
    turtle.forward(12)
    turtle.right(90)
    turtle.forward(7)
    turtle.right(90)
    turtle.forward(12)
    turtle.right(180)
    turtle.forward(12)
    turtle.up()
    turtle.goto(0, 0)


def hard():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(10)
    turtle.up()
    turtle.goto(0, 0)


def soft():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(30)
    turtle.up()
    turtle.goto(0, 0)


def iy():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(30)
    turtle.up()
    turtle.setheading(180)
    turtle.forward(5)
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(30)
    turtle.up()
    turtle.goto(0, 0)


def ie():
    turtle.down()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.up()
    turtle.goto(0, 0)


def iu():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.up()
    turtle.left(180)
    turtle.forward(25)
    turtle.down()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()
    turtle.goto(0, 0)


def ja():
    turtle.down()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.setheading(245)
    turtle.forward(17)
    turtle.up()
    turtle.goto(0, 0)
# Функции букв: конец


def open():
    turtle.up()
    poz = 0
    for ltt in Word_clean:
        poz += 1
        if ltt == 'а':
            turtle.goto(coordinates[poz], 5)
            a()
        elif ltt == 'б':
            turtle.goto(coordinates[poz], 5)
            bbb()
        elif ltt == 'в':
            turtle.goto(coordinates[poz], 5)
            b()
        elif ltt == 'г':
            turtle.goto(coordinates[poz], 5)
            g()
        elif ltt == 'д':
            turtle.goto(coordinates[poz], 5)
            d()
        elif ltt == 'е':
            turtle.goto(coordinates[poz], 5)
            e()
        elif ltt == 'ё':
            turtle.goto(coordinates[poz], 5)
            e()
        elif ltt == 'ж':
            turtle.goto(coordinates[poz], 5)
            j()
        elif ltt == 'з':
            turtle.goto(coordinates[poz], 5)
            tri()
        elif ltt == 'и':
            turtle.goto(coordinates[poz], 5)
            iii()
        elif ltt == 'й':
            turtle.goto(coordinates[poz], 5)
            iii()
        elif ltt == 'к':
            turtle.goto(coordinates[poz], 5)
            k()
        elif ltt == 'л':
            turtle.goto(coordinates[poz], 5)
            ll()
        elif ltt == 'м':
            turtle.goto(coordinates[poz], 5)
            m()
        elif ltt == 'н':
            turtle.goto(coordinates[poz], 5)
            n()
        elif ltt == 'о':
            turtle.goto(coordinates[poz], 5)
            o()
        elif ltt == 'п':
            turtle.goto(coordinates[poz], 5)
            p()
        elif ltt == 'р':
            turtle.goto(coordinates[poz], 5)
            r()
        elif ltt == 'с':
            turtle.goto(coordinates[poz], 5)
            s()
        elif ltt == 'т':
            turtle.goto(coordinates[poz], 5)
            t()
        elif ltt == 'у':
            turtle.goto(coordinates[poz], 5)
            u()
        elif ltt == 'ф':
            turtle.goto(coordinates[poz], 5)
            f()
        elif ltt == 'х':
            turtle.goto(coordinates[poz], 5)
            h()
        elif ltt == 'ц':
            turtle.goto(coordinates[poz], 5)
            c()
        elif ltt == 'ч':
            turtle.goto(coordinates[poz], 5)
            ch()
        elif ltt == 'ш':
            turtle.goto(coordinates[poz], 5)
            sh()
        elif ltt == 'щ':
            turtle.goto(coordinates[poz], 5)
            sch()
        elif ltt == 'ъ':
            turtle.goto(coordinates[poz], 5)
            hard()
        elif ltt == 'ь':
            turtle.goto(coordinates[poz], 5)
            soft()
        elif ltt == 'ы':
            turtle.goto(coordinates[poz], 5)
            iy()
        elif ltt == 'э':
            turtle.goto(coordinates[poz], 5)
            ie()
        elif ltt == 'ю':
            turtle.goto(coordinates[poz], 5)
            iu()
        elif ltt == 'я':
            turtle.goto(coordinates[poz], 5)
            ja()
        else:
            continue


turtle.Screen().screensize(650, 670)
turtle.speed(0)
turtle.pensize(3)
time.sleep(2)

# Рисование барабана: начало
turtle.up()
turtle.goto(325, -350)
turtle.setheading(90)
turtle.down()
turtle.forward(1000)
turtle.up()
turtle.goto(240, -350)
turtle.setheading(90)
turtle.down()
turtle.forward(1000)
turtle.goto(240, 0)
turtle.setheading(0)
turtle.forward(85)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(85)
turtle.up()
turtle.goto(0, 0)
# Рисование барабана: конец


Question = randint(0, len(Questions)-1)
word = Words[Question]
Word = []
for letter in word:
    Word.append(letter)
# Word = ['и', 'н', 'ф', 'л', 'я', 'ц', 'и', 'я']
Word_clean = []
for i in range(len(Word)):
    Word_clean.append('')
# Word_clean = ['', '', '', '', '', '', '', '']

# Рисование ячеек для букв: начало
turtle.up()
turtle.goto(-300, 0)
turtle.setheading(0)
for square in range(len(Word)):
    squares()
# Рисование ячеек для букв: конец
ug = 0

# Якубович:
print('Добрый вечер, здравствуйте, уважаемые дамы и господа! В эфире капитал-шоу Поле чудес!')
time.sleep(2)
print('Первая тройка игроков в студию!')
time.sleep(2)
print('Первый игрок, представьтесь')
Player_1 = input()
print('Здравствуйте,', Player_1)
time.sleep(2)
print('Второй игрок, представьтесь')
Player_2 = input()
print('Здравствуйте,', Player_2)
time.sleep(2)
print('Третий игрок, представьтесь')
Player_3 = input()
print('Здравствуйте,', Player_3)
Players = (Player_1, Player_2, Player_3)
Points = [0, 0, 0]
Presents = [[], [], []]
win = 0
winner = ''
number = 0

while True:
    for hod in Players:
        if hod == Players[0]:
            number = 0
        elif hod == Players[1]:
            number = 1
        elif hod == Players[2]:
            number = 2
        winner = hod
        time.sleep(1)
        print('Внимание вопрос!')
        print(Questions[Question])
        time.sleep(2)
        print(hod, ', ваш ход', sep='')
        # вращение барабана
        print('Вращайте барабан! (Enter)')
        drum()
        # вращение барабана
        print("Скажите слово сразу или будете открывать буквы? (1 или 0)")
        Choice = input()
        if Choice == '1':
            print('Итак слово...')
            Choice = input()
            if Choice == word:
                print('И...')
                time.sleep(3)
                print('...перед нами победитель!')
                time.sleep(2)
                if Points[number] == 0:
                    print(hod, ', Вам присваивается 100000 очков')
                    Points[number] = 100000
                else:
                    print(hod, ', Ваши очки умножены на 10')
                    Points[number] *= 10
                win = 1
                break
            else:
                print('И...')
                time.sleep(3)
                print('...это неправильный ответ!')
                time.sleep(2)
                print('Ход переходит к следующему игроку')
                time.sleep(1)
                continue
        elif Choice == '0':
            while True:
                print('Итак буква..')
                Choice = input()
                for ltr in Word:
                    if Choice == ltr:
                        print('Откройте букву', Choice)
                        ug = 1
                        for Let in Word:
                            if Choice == Let:
                                Id = Word.index(Choice)
                                Word_clean[Id] = Word[Id]
                                Word[Id] = ''
                        open()
                if Word_clean.count('') == 0:
                    time.sleep(1)
                    print('И перед нами победитель!')
                    time.sleep(1)
                    print(hod, ', Ваши очки умножены на 10')
                    Points[number] *= 10
                    time.sleep(1)
                    win = 1
                    break
                if ug == 1:
                    print('Вы правильно угадали букву')
                    ug = 0
                    print('Назовите ещё букву')
                elif ug == 0:
                    print('Такой буквы нет')
                    break
            if win == 1:
                break
            else:
                print('Ход переходит к следующему игроку')
                continue
    if win == 1:
        break
time.sleep(1)
print('Победитель сегодняшней игры', winner, '\n', 'он уходит с', Points[number], 'очков')
if len(Presents[2]) != 0:
    print('А также с', end='')
    for i in Presents[3]:
        print(i)
time.sleep(3)
print('До новых встреч, уважаемые дамы и господа, в эфире было капитал-шоу Поле чудес')
time.sleep(20)
