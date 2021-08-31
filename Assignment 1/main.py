"""
Assignment 1
Author: Sagi Biran
ID: 205620859
"""


# ------------------------------------------------
#                       Q#1
# ------------------------------------------------
def printLandingTime(hrs, mins, secs, fTime):
    if hrs < 0 or mins < 0 or secs < 0 or fTime < 0:
        print('Invalid Input was entered!')
    else:
        secs += fTime
        mins += int(secs / 60)
        secs = secs % 60
        hrs += int(mins / 60)
        mins = mins % 60
        hour, minute, second, days = 'hour', 'minute', 'second', ''
        if hrs > 24:
            days = '(+' + str(int(hrs / 24)) + ' day'
            if int(hrs / 24) == 1:
                days += ')'
            elif int(hrs / 24) > 1:
                days += 's)'
            hrs = hrs % 24
        if hrs > 1:
            hour += 's'
        if mins > 1:
            minute += 's'
        if secs > 1:
            second += 's'
        if mins == 0 and secs == 0:
            mins, minute, secs, second = 'exactly', '', '', ''
        print("Landing Time:", hrs, hour, mins, minute, secs, second, days)


# ------------------------------------------------
#                       Q#2
# ------------------------------------------------
def printPrevDay(day, month, year):
    day -= 1
    if day == 0:
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = 31
        elif month in [4, 6, 9, 11]:
            day = 30
        else:
            day = 28
        if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month == 2:
            day += 1
    print('{:02d}/{:02d}/{:4}'.format(day, month, year))


# ------------------------------------------------
#                       Q#3
# ------------------------------------------------
def ifOrder(givenNumber):
    indicator = -1
    while givenNumber:
        if givenNumber % 2 == 0:
            if indicator == 0:
                return False
            indicator = 0
        else:
            if indicator == 1:
                return False
            indicator = 1
        givenNumber //= 10
    return True


# ------------------------------------------------
#                       Q#4
# ------------------------------------------------
def printFigure(n):
    tempDigit = 1
    if n > 0 and isinstance(n, int) and 1 < n < 19 and n % 2 != 0:
        for a1 in range(1, (n + 1) // 2 + 1):
            for a2 in range((n + 1) // 2 - a1):
                print(" ", end="")
            for a3 in range((a1 * 2) - 1):
                print(tempDigit, end="")
                if tempDigit == n:
                    tempDigit = 0
                tempDigit += 1
            print()

        for a1 in range((n + 1) // 2 + 1, n + 1):
            for a2 in range(a1 - (n + 1) // 2):
                print(" ", end="")
            for a3 in range((n + 1 - a1) * 2 - 1):
                print(tempDigit, end="")
                if tempDigit == n:
                    tempDigit = 0
                tempDigit += 1
            print()
    else:
        print("parameter error")


# ------------------------------------------------
#                       Q#5
# ------------------------------------------------
def printRange(start, stop=None, step=1):
    if stop is None:
        for i in range(start):
            print(i, end=" ")
        return ""

    if step >= 0:
        if start >= stop:
            return
        print(start, end=" ")
        printRange(start + step, stop, step)
    else:
        if start <= stop:
            return
        print(start, end=" ")
        printRange(start + step, stop, step)
    return ""


# ------------------------------------------------
#                       Q#6
# ------------------------------------------------
def doRepeat(Number, repeat=None):
    if repeat == 0:
        return "{:n}".format(0)
    if repeat == 1 or repeat is None:
        return "{:n}".format(Number)
    else:
        repeat -= 1
        return "{:n}".format(Number) + doRepeat(Number, repeat)


# ------------------------------------------------
#                       Q#7
# ------------------------------------------------
def sumDigits(x):
    if x == 0:
        return 0
    else:
        return x % 10 + sumDigits(int(x / 10))


def calcNumValue(num):
    if countDigits(sumDigits(num)) == 1:
        return sumDigits(num)
    else:
        return calcNumValue(sumDigits(num))


def countDigits(x):
    if x < 10:
        return 1
    else:
        return 1 + countDigits(int(x / 10))


# ------------------------------------------------
#                       Q#8
# ------------------------------------------------
def doReverse(num):
    if countDigits(num) == 1:
        return num
    else:
        return (num % 10) * pow(10, countDigits(num) - 1) + doReverse(int(num / 10))


# ------------------------------------------------
#                       Driver
# ------------------------------------------------
def driver():
    print('Q#1')
    printLandingTime(23, 5, 0, 10)
    printLandingTime(0, 0, 0, 177615)
    printLandingTime(17, 59, 55, 5)
    print('\nQ#2')
    printPrevDay(11, 7, 2021)
    printPrevDay(1, 3, 2012)
    printPrevDay(1, 3, 2015)
    printPrevDay(1, 8, 2021)
    printPrevDay(1, 1, 2021)
    print('\nQ#3')
    print(ifOrder(12345))
    print(ifOrder(264))
    print(ifOrder(1573))
    print(ifOrder(2785))
    print(ifOrder(2))
    print('\nQ#4')
    printFigure(9)
    printFigure(10)
    print('\nQ#5')
    printRange(6, 20, 3)
    print()
    printRange(6, 20, -3)
    print()
    printRange(20, 6, -3)
    print()
    printRange(6, 10)
    print()
    printRange(6)
    print()
    print('\nQ#6')
    print(doRepeat(3, 5))
    print(doRepeat(7, 2))
    print(doRepeat(7))
    print(doRepeat(7, 0))
    print('\nQ#7')
    print(calcNumValue(15))
    print(calcNumValue(1589))
    print(calcNumValue(15893476))
    print(calcNumValue(1))
    print(calcNumValue(15893476987))
    print('\nQ#8')
    print(doReverse(12345))
    print(doReverse(5))
    print(doReverse(726451))


driver()
'''
Q#1
Landing Time: 23 hours, 5 minutes, 10 seconds
Landing Time: 1 hour, 20 minutes, 15 seconds(+2 days)
Landing Time: 18 hours exactly

Q#2
10/07/2021
29/02/2012
28/02/2015
31/07/2021
31/12/2020

Q#3
True
False
False
True
True

Q#4
        1
       234
      56789
     1234567
    891234567
     8912345
      67891
       234
        5
parameter error

Q#5
6 9 12 15 18 

20 17 14 11 8 
6 7 8 9 
0 1 2 3 4 5 

Q#6
33333
77
7
0

Q#7
6
5
7
1
4

Q#8
54321
5
154627
>>> 
'''
