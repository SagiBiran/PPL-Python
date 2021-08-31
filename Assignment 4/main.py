"""
Assignment 4
Author: Sagi Biran
ID: 205620859
"""

# ------------------------------------------------
#                       Q#1
# ------------------------------------------------
# ------------------------------------------------
from functools import reduce
from operator import mul

monthDict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
             9: 'September', 10: 'October', 11: 'November', 12: 'December'}


class Date(object):
    """
    Class Date that included year,month and a day in month
    """

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        """
        :return: string representation of Date object.
        """
        if self.day == 1:
            return f"'{self.day}st of {monthDict[self.month]},{self.year}'"
        elif self.day == 2:
            return f"'{self.day}nd of {monthDict[self.month]},{self.year}'"
        elif self.day == 3:
            return f"'{self.day}rd of {monthDict[self.month]},{self.year}'"
        else:
            return f"'{self.day}th of {monthDict[self.month]},{self.year}'"

    def __repr__(self):
        """
        :return:  python's string representation of Date object.
        """
        return 'Date({0},{1},{2})'.format(self.year, self.month, self.day)


class Time(object):
    """
    Class Time that included hour ane minute
    """

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        """
        :return: string representation of Time object.
        """
        return f'{self.hour}:{self.minute}0'

    def __repr__(self):
        """
        :return:  python's string representation of Time object.
        """
        return 'Time({0},{1})'.format(self.hour, self.minute)


class CalendarEntry(object):
    """
    Schedule Class that record number of to-do list (with start time and end time)  two tasks with exactly the same
    times is not allowed
    """

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.tasks = {}

    def addTask(self, assignmentName, startTime, endingTime):
        """
        funtion will add assignment into tasks dictionary
        :param assignmentName: assignment name
        :param startTime: starting time of the assignment
        :param endingTime: ending time of the assignment
        :return: none
        """
        if (str(startTime), str(endingTime)) in self.tasks.keys():
            return print(
                "\n---ERROR! there is no 2 assignments in the exact times!\nhence last assignment didn't recorded!---\n")
        self.tasks[(str(startTime), str(endingTime))] = assignmentName

    def __str__(self):
        """
        :return: string representation of CalendarEntry object.
        """
        i = 1
        print('Todo list for {0}th of {1}, {2}:'.format(self.day, monthDict[self.month], self.year))
        for key in self.tasks.keys():
            print(str(i) + '. ' + str(key[0]) + '-' + str(key[1]) + ' - ' + self.tasks[key])
            i += 1
        return ''

    def __repr__(self):
        """
        :return:  python's string representation of CalendarEntry object.
        """
        return 'CalendarEntry({0},{1},{2})'.format(self.year, self.month, self.day)


# today = Date(2021, 8, 15)
# print(repr(today))
# print(repr(today.year))
# print(today)
# todo = CalendarEntry(2021, 8, 15)
# t = Time(10, 0)
# print(t)
# todo.addTask("PPL lecture", t, Time(13, 0))
# todo.addTask("PPL lecture", t, Time(13, 0))
# todo.addTask("PPL homework#4", Time(14, 0), Time(16, 0))
# print(repr(todo.tasks))
# print(todo)


# ------------------------------------------------
#                       Q#2
# ------------------------------------------------
def make_class(attrs, base=None):
    """
    Our custom OOP.
    :param attrs: attrs variable that store attributes for instance
    :param base: base class that current class may inherit from
    :return: new class (a dispatch dictionary) with given class attributes
    """

    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    def set(name, value):
        attrs[name] = value

    def new(*args):
        attrs = {}

        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        def set(name, value):
            attrs[name] = value

        obj = {'get': get, 'set': set}
        init = get('__init__')
        if init: init(*args)

        return obj

    cls = {'get': get, 'set': set, 'new': new}
    return cls


# ------------------------------------------------
def make_date_class():
    """
    Implement Date Class in Shmython
    """

    def __init__(self, y, m, d):
        self['set']('year', y)
        self['set']('month', m)
        self['set']('day', d)

    def __str__(self):
        """
        :param self: current date object
        :return: string representation of Date object.
        """
        return '%02d/%02d/%d' % (self['get']('day'), self['get']('month'), self['get']('year'))

    return make_class(locals())


# Date = make_date_class()
# today = Date['new'](2021, 8, 15)
# print(today['get']('year'))

# ------------------------------------------------
def make_time_class():
    """
    Implement Time Class in Shmython
    """

    def __init__(self, hour, minute):
        self['set']('hour', hour)
        self['set']('minute', minute)

    def __str__(self):
        """
        :param self: current time object
        :return: string representation of Time object.
        """
        return str(self['get']('hour')) + ':' + str(self['get']('minute')) + '0'

    return make_class(locals())


# ------------------------------------------------
def make_calentry_class():
    """
    Implement calentry Class in Shmython
    """
    tasks = {}

    def __init__(self, y, m, d):
        self['set']('year', y)
        self['set']('month', m)
        self['set']('day', d)
        self['set']('tasks', tasks)

    def addTask(self, assignmentName, startTime, endingTime):
        """
        funtion will add assignment into tasks dictionary
        :param self: Calentry object
        :param assignmentName: assignment name
        :param startTime: starting time of the assignment
        :param endingTime: ending time of the assignment
        :return: none
        """
        self['get']('tasks')[(startTime['get']('__str__')(), endingTime['get']('__str__')())] = assignmentName

    def __str__(self):
        """
        :param self: current Calentry object
        :return: string representation of Calentry object.
        """
        return self['get']('tasks')

    return make_class(locals())


# CalendarEntry = make_calentry_class()
# todo = CalendarEntry['new'](2021, 8, 15)
# Time = make_time_class()
# t = Time['new'](10, 0)
# print(t['get']('__str__')())
# todo['get']('addTask')('PPL lecture', t, Time['new'](13, 0))
# todo['get']('addTask')('PPL homework#4', Time['new'](14, 0), Time['new'](16, 0))
# print(todo['get']('tasks'))
# ------------------------------------------------
#                       Q#3
# ------------------------------------------------

# --------------------------------------Shekel-------------------------------------- #
class Shekel(object):
    """
    Class that implement a Shekel coin currency in Israel Banks
    """

    def __init__(self, shekelCurrency):
        self.shekelCurrency = shekelCurrency

    def amount(self):
        """
        :return: current currency for Israeli Shekel Coin
        """
        return self.shekelCurrency

    def __str__(self):
        """
        :return: string representation of Shekel object.
        """
        return f'{self.amount()}nis'

    def __repr__(self):
        """
        :return: python's string representation of Shekel object.
        """
        return 'Shekel({0:.1f})'.format(self.shekelCurrency)


# --------------------------------------Euro-------------------------------------- #
class Euro(object):
    """
    Class that implement a Euro coin currency in Israel Banks
    """

    def __init__(self, euroCurrency):
        self.shekelCurrency = euroCurrency * rates[('euro', 'nis')]
        self.euroCurrency = euroCurrency

    def amount(self):
        """
        :return: current currency for EURO coin in Shekels!
        """
        return self.shekelCurrency

    def updateEuroCurrency(self, euroCurrency):
        """
        :param euroCurrency:
        :return: a new object with Shekel and Euro attributes update due change made by user
        """
        self.euroCurrency = euroCurrency
        self.shekelCurrency = euroCurrency * rates[('euro', 'nis')]

    def __str__(self):
        """
        :return: string representation of Euro object.
        """
        return f'{self.euroCurrency:.1f}€'

    def __repr__(self):
        """
        :return: python's string representation of Euro object.
        """
        return 'Euro({0})'.format(self.euroCurrency)


# --------------------------------------Dollar-------------------------------------- #

class Dollar(object):
    def __init__(self, dollarCurrency):
        self.shekelCurrency = dollarCurrency * rates[('dollar', 'nis')]
        self.dollarCurrency = dollarCurrency

    def amount(self):
        """
        :return: current currency for Dollar coin in Shekels!
        """
        return self.shekelCurrency

    def updateDollarCurrency(self, dollarCurrency):
        """
        :return: a new object with Shekel and Dollar attributes update due change made by user
        """
        self.dollarCurrency = dollarCurrency
        self.shekelCurrency = dollarCurrency * rates[('dollar', 'nis')]

    def __str__(self):
        """
        :return: string representation of Dollar object.
        """
        return f'{self.dollarCurrency:.1f}$'

    def __repr__(self):
        """
        :return: python's string representation of Dollar object.
        """
        return 'Dollar({0})'.format(self.dollarCurrency)


Shekel.__add__ = lambda self, other: add_shekels(self, other)
Euro.__add__ = lambda self, other: add_euros(self, other)
Dollar.__add__ = lambda self, other: add_dollars(self, other)
Shekel.__sub__ = lambda self, other: sub_shekels(self, other)
Euro.__sub__ = lambda self, other: sub_euros(self, other)
Dollar.__sub__ = lambda self, other: sub_dollars(self, other)


# --------------------------------------
# Generic Functions
# --------------------------------------
def add_shekels(s1, s2):
    """
    :param s1: first Shekel object
    :param s2: second Shekel object
    :return: summation of two Shekel Objects
    """
    return Shekel(s1.amount() + s2.amount())


def sub_shekels(s1, s2):
    """
    :param s1: first Shekel object
    :param s2: second Shekel object
    :return: substitution of two Shekel Objects
    """
    return Shekel(s1.amount() - s2.amount())


def add_euros(e1, e2):
    """
    :param e1: first Euro object
    :param e2: second Euro object
    :return: summation of two Euro Objects
    """
    return Shekel(e1.amount() + e2.amount())


def sub_euros(e1, e2):
    """
    :param e1: first Euro object
    :param e2: second Euro object
    :return: substitution of two Euro Objects
    """
    return Shekel(e1.amount() - e2.amount())


def add_dollars(d1, d2):
    """
    :param d1: first Dollar object
    :param d2: second Dollar object
    :return: summation of two Dollar Objects
    """
    return Shekel(d1.amount() + d2.amount())


def sub_dollars(d1, d2):
    """
    :param d1: first Dollar object
    :param d2: second Dollar object
    :return: substitution of two Dollar Objects
    """
    if type(d1) != Shekel:
        d1 = dollars_or_euros_to_shekels(d1)
    if type(d2) != Shekel:
        d2 = dollars_or_euros_to_shekels(d2)
    return Shekel(d1.amount() - d2.amount())


# ----------------------------------------------------------
def add_shekels_and_other(s1, o2):
    """
    :param s1: Shekel Object
    :param o2: Euro/Dollar Object
    :return: Shekel object after applying summation generic function on o2 parameter
    """
    return Shekel(s1.amount() + o2.amount())


def sub_shekels_and_other(s1, o2):
    """
    :param s1: Shekel Object
    :param o2: Euro/Dollar Object
    :return: Shekel object after applying substitution generic function on o2 parameter
    """
    return Shekel(s1.amount() + o2.amount())


def add_dollar_and_euro(d1, e1):
    """
    :param d1: Dollar Object
    :param e1: Euro Object
    :return: Dollar Object that return accurate result from doing summation between Dollar coin and Euro Coin
    """
    e1.euroCurrency *= rates[('euro', 'dollar')]
    return Dollar(d1.dollarCurrency + e1.euroCurrency)


def sub_dollars_and_euros(d1, e1):
    """
    :param d1: Dollar Object
    :param e1: Euro Object
    :return: Dollar Object that return accurate result from doing substitution between Dollar coin and Euro Coin
    """
    e1.euroCurrency *= rates[('euro', 'dollar')]
    return Dollar(d1.dollarCurrency - e1.euroCurrency)


def sub_dollars_and_shekels(d1, s1):
    """
    :param d1: Dollar Object
    :param s1: Shekel Object
    :return: Dollar Object that return accurate result from doing summation between Dollar coin and Shekel Coin
    """
    s1.amount *= rates[('dollar', 'nis')]
    return Dollar(d1.dollarCurrency - s1.amount())


# ----------------------------------------------------------
def add_euro_and_dollar(e1, d1):
    """
    :param e1: Euro Object
    :param d1: Dollar Object
    :return: Euro Object that return accurate result from doing summation between Dollar coin and Euro Coin
    """
    d1.dollarCurrency *= 0.85
    return Euro(e1.euroCurrency + d1.dollarCurrency)


def sub_euros_and_dollars(e1, d1):
    """
    :param e1: Euro Object
    :param d1: Dollar Object
    :return: Euro Object that return accurate result from doing substitution between Dollar coin and Euro Coin
    """
    d1.dollarCurrency *= 0.85
    return Euro(e1.euroCurrency - d1.dollarCurrency)


def sub_euros_and_shekels(e1, s1):
    """
    :param e1: Euro Object
    :param s1: Shekel Object
    :return: Euro Object that return accurate result from doing substitution between Shekel coin and Euro Coin
    """
    s1.amount *= rates[('euro', 'nis')]
    return Euro(e1.euroCurrency - s1.amount())


def type_tag(x):
    """
    :param x: Shekel/Euro/Dollar object
    :return: the type of given argument
    """
    return type_tag.tags[type(x)]


# known tags
type_tag.tags = {Shekel: 'shekel', Euro: 'euro', Dollar: 'dollar'}


def add(z1, z2):
    """
    Generic function that gets two objects (could be the same or not) and do summation between theses two,
    objects cloud be from Shekel,Euro and Dollar Classes
    :param z1: Shekel/Euro/Dollar object
    :param z2: Shekel/Euro/Dollar object
    :return: summation between two different objects (could be that same)
    """
    types = (type_tag(z1), type_tag(z2))
    return add.implementations[types](z1, z2)


# dictionary that has tags for coins as a tuple in key and operation function as value
add.implementations = {('shekel', 'shekel'): add_shekels,
                       ('shekel', 'euro'): add_shekels_and_other,
                       ('shekel', 'dollar'): add_shekels_and_other,
                       ('dollar', 'dollar'): add_dollars,
                       ('dollar', 'euro'): add_dollar_and_euro,
                       ('dollar', 'shekel'): lambda x, y: add_shekels_and_other(y, x),
                       ('euro', 'euro'): add_euros,
                       ('euro', 'dollar'): add_euro_and_dollar,
                       ('euro', 'shekel'): lambda x, y: add_shekels_and_other(y, x)}


# ------------------------------------------------
#                       Q#4
# ------------------------------------------------
# --------------------------------------
# Data-directed programming
# --------------------------------------
def apply(operator_name, x, y):
    """
    :param operator_name: 'sub'/'add'
    :param x:  Shekel/Euro/Dollar object
    :param y: Shekel/Euro/Dollar object
    :return: desired result between two "operands"
    """
    tags = (type_tag(x), type_tag(y))
    key = (operator_name, tags)
    return apply.implementations[key](x, y)


apply.implementations = {('sub', ('dollar', 'euro')): sub_dollars_and_euros,
                         ('sub', ('dollar', 'shekel')): sub_dollars_and_shekels,
                         ('sub', ('euro', 'dollar')): sub_euros_and_dollars,
                         ('sub', ('euro', 'shekel')): sub_euros_and_shekels,
                         ('sub', ('shekel', 'euro')): sub_shekels_and_other,
                         ('sub', ('shekel', 'dollar')): sub_shekels_and_other,
                         }
adders = add.implementations.items()
apply.implementations.update({('add', tags): fn for (tags, fn) in adders})


# ------------------------------------------------
#                       Q#5
# ------------------------------------------------
# --------------------------------------
# Coercion
# --------------------------------------
def dollars_or_euros_to_shekels(x):
    """
    :param x: Dollar Object
    :return: Shekel object after doing conversation on Dollar object
    """
    return Shekel(x.amount())


def euros_to_dollars(x):
    """
    :param x: Euro Object
    :return: Dollar object after doing conversation on Euro object
    """
    x.updateEuroCurrency(x.euroCurrency * rates[('euro', 'dollar')])
    return Dollar(x.euroCurrency)


def dollars_to_euros(x):
    """
    :param x: Dollar Object
    :return: Shekel object after doing conversation on Dollar object
    """
    x.updateDollarCurrency(x.dollarCurrency * 0.85)
    return Shekel(x.amount())


coercions = {
    ('shekel', 'dollar'): dollars_or_euros_to_shekels,
    ('shekel', 'euro'): dollars_or_euros_to_shekels,
    ('nis', 'dollar'): dollars_or_euros_to_shekels,
    ('nis', 'euro'): dollars_or_euros_to_shekels,
    ('dollar', 'nis'): dollars_or_euros_to_shekels,
    ('dollar', 'shekel'): dollars_or_euros_to_shekels,
    ('euro', 'shekel'): dollars_or_euros_to_shekels,
    ('euro', 'nis'): dollars_or_euros_to_shekels,
    ('euro', 'dollar'): euros_to_dollars,
}


def coerce_apply(operator_name, x, y):
    """
    :param operator_name: 'sub' or 'add'
    :param x: Shekel/Euro/Dollar object
    :param y: Shekel/Euro/Dollar object
    :return: appropriate function for summation or substitution due
    coerce apply dictionary.
    """
    tx, ty = type_tag(x), type_tag(y)
    if tx != ty:
        if (tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercion possible.'
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)


coerce_apply.implementations = {('sub', 'shekel'): sub_shekels,
                                ('sub', 'euro'): sub_euros,
                                ('sub', 'dollar'): sub_dollars,
                                ('add', 'shekel'): add_shekels,
                                ('add', 'euro'): add_euros,
                                ('add', 'dollar'): add_dollars, }

rates = {('dollar', 'nis'): 3.22, ('euro', 'nis'): 3.81}
# s = Shekel(50)
# d = Dollar(50)
# e = Euro(50)
# print(d.amount())
# print(e.amount())
# print(repr(d + s))
# print(d + s)
# z = eval(repr(d))
# print(z)
# print(s)
# print(e)
# print(repr(apply('add', Shekel(50), Dollar(20))))
rates[('euro', 'dollar')] = 1.183


# print(repr(apply('add', Dollar(50), Euro(20))))
# print(repr(apply('sub', Dollar(50), Euro(20))))
# print(repr(coercions[('dollar', 'nis')](Dollar(50))))
# rates[('euro', 'dollar')] = 1.183
# print(repr(coerce_apply('add', Shekel(50), Dollar(20))))
# print(repr(coerce_apply('sub', Dollar(50), Euro(20))))
# ------------------------------------------------
#                       Q#6
# ------------------------------------------------
def parking(pHour, regularCapacity, priorityCapacity, vipCapacity):
    """Return a dispatch function that represents a bank account."""
    try:
        assert pHour > 0
    except AssertionError:
        print("the price value is bad")
    try:
        assert regularCapacity > 0
        assert priorityCapacity > 0
        assert vipCapacity > 0
    except AssertionError:
        print("parking places error")

    parkingCapacity = {'Regular': regularCapacity, 'Priority': priorityCapacity,
                       'VIP': vipCapacity}
    parkingDetails = {'Regular': [], 'Priority': [], 'VIP': []}
    lstParkingDetails = []

    def print_list():
        """
        :return: function will print details of all cars located in parking
        """
        lstParkingDetails.reverse()

        def next():
            """
            :return: all cars in parking.
            """
            try:
                tmpElement = lstParkingDetails.pop()
                print(f'car: {tmpElement[0]}, parking type: {str(tmpElement[1])}, parking time: {tmpElement[2]}')
            except IndexError:
                print("no car")

        return {'next': next}

    def print_parking(parkingType):
        """
        :param parkingType: 'Regular'/'Priority'/'VIP'
        :return: all cars located in parking
        """
        for ele in parkingDetails[parkingType]:
            print(f'car: {ele[0]}, parking time: {ele[2]}')

    def next_time():
        """
        :return: increase one house for parking time to each car in parking
        """
        for parkingType, car in parkingDetails.items():
            if len(car) != 0:
                for parkingTime in car:
                    parkingTime[2] += 1
                for specificCar in lstParkingDetails:
                    specificCar[2] += 1

    def start_parking(carNumber, parkingType):
        """
        :param carNumber: car number that entering into parking
        :param parkingType: Type of entered car
        :return: a car entrance in parking
        """
        try:
            val = int(carNumber)
            keyChecking = parkingDetails[parkingType]
            for carType in parkingDetails.keys():
                if parkingType == carType:
                    if parkingCapacity[carType] == 0:
                        return print(f'{carType} parking is full')
                    else:
                        parkingDetails[carType].append([carNumber, parkingType, 1])
                        lstParkingDetails.append([carNumber, parkingType, 1])
                        parkingCapacity[carType] -= 1
                    break
        except KeyError:
            print(parkingType + " is incorrect parking type")
        except ValueError:
            print("incorrect car number")

    def end_parking(carNumber):
        """
        :param carNumber: car number of exiting car
        :return: going out operation on car that parked in parking
        """
        for parkingType, cars in parkingDetails.items():
            if len(cars) != 0:
                for car in cars:
                    if carNumber == car[0]:
                        print(
                            f'car: {car[0]}, parking type: {str(car[1])}, parking time: {car[2]}\npayment: {car[2] * pHour}')
                        cars.remove(car)
                        return
        return print(f'car not found')

    dispatch = {'print_list': print_list, 'print_parking': print_parking, 'next_time': next_time,
                'start_parking': start_parking, 'end_parking': end_parking}

    return dispatch


# park1 = parking(-10, 3, 3, 3)
# park1 = parking(10, 0, 3, 3)
# # print(repr(park1))
# park1 = parking(10, 3, 3, 3)
# park1['start_parking']('aaa', 'VIP')
# park1['start_parking'](223, 'VIP1')
# park1['start_parking'](222, 'Regular')
# park1['start_parking'](223, 'Regular')
# park1['next_time']()
# park1['start_parking'](224, 'Regular')
# park1['start_parking'](225, 'VIP')
# prn = park1['print_list']()
# print(repr(prn))
# for _ in range(6):
#     prn['next']()
# ------------------------------------------------
#                       Q#7
# ------------------------------------------------
class Expr(object):
    """
    Class Expr will represent an arithmetic expression where arguments could be expressions.
    the leaves could be belong to any kind but not Expr
    """

    def __init__(self, entry, left=None, right=None):
        self.operator = entry
        self.left = left
        self.right = right

    def __repr__(self):
        """
        :return: python's string repression of Expr object
        """
        args = repr(self.operator)
        if type(self.left) and type(self.right) == tuple:
            complexLeft = Expr(self.left[0], self.left[1], self.left[2])
            complexRight = Expr(self.right[0], self.right[1], self.right[2])
            args += ',{0},{1}'.format(repr(complexLeft), repr(complexRight))
        elif type(self.left) == tuple:
            complexLeft = Expr(self.left[0], self.left[1], self.left[2])
            args += ',{0},{1}'.format(repr(complexLeft), repr(self.right))
        elif type(self.right) == tuple:
            complexRight = Expr(self.right[0], self.right[1], self.right[2])
            args += ',{0},{1}'.format(repr(self.left), repr(complexRight))
        else:
            args += ',{0},{1}'.format(repr(self.left), repr(self.right))
        return 'Expr({0})'.format(args)


def buildExprTree(specialTuple):
    """
    :param specialTuple: tuple with 3 elements(1- operator name, 2,3- arithmetic expressions
    :return: finished build first and than return Expr Instance for the given expression
    """
    operator = specialTuple[0]
    firstOperand = specialTuple[1]
    secondOperand = specialTuple[2]
    return Expr(operator, firstOperand, secondOperand)


# exp = buildExprTree(('add', ('mul', 2, 3), 10))
# exp = buildExprTree(('add', ('mul', 2, 3), ('mul', 2, 3)))
# print(repr(exp))
# Expr('add',Expr('mul',2,3),10)
# ------------------------------------------------
#                       Q#8
# ------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
##############################
# read_eval_print_loop could #
# use as "driver"            #
##############################
def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return


# ----------------------------------------------------------------------------------------------------------------------
##############################
#     Exp Class              #
##############################
class Exp(object):
    """A call expression in Calculator."""
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)


# ----------------------------------------------------------------------------------------------------------------------
##############################
# Eval & Apply               #
##############################

def calc_eval(exp):
    """Evaluate a Calculator expression."""
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def calc_apply(operator, args):
    """Apply the named operator to a list of args."""
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])

    if operator == 'int':
        if args[1] == 2:
            ar = [int(i) for i in str(args[0])]
            ar = ar[::-1]
            res = []
            for i in range(len(ar)):
                res.append(ar[i] * (2 ** i))
            sum_res = sum(res)
            return sum_res
        elif args[1] == 8:
            num = args[0]
            dec_value = 0
            base = 1
            temp = num
            while temp:
                last_digit = temp % 10
                temp = int(temp / 10)
                dec_value += last_digit * base
                base = base * 8
            return dec_value
        elif args[1] == 16:
            num = str(args[0])
            c = count = i = 0
            hexLength = len(num) - 1
            while hexLength >= 0:
                if '0' <= num[hexLength] <= '9':
                    rem = int(num[hexLength])
                elif 'A' <= num[hexLength] <= 'F':
                    rem = ord(num[hexLength]) - 55
                elif 'a' <= num[hexLength] <= 'f':
                    rem = ord(num[hexLength]) - 87
                else:
                    c = 1
                    break
                count = count + (rem * (16 ** i))
                hexLength = hexLength - 1
                i = i + 1
            return count
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numerator, denominator = args
        return numerator / denominator
    if operator in ('compl', '!'):
        if len(args) > 1:
            raise TypeError(operator + ' requires at least 1 argument')
        if not isinstance(args[0], int):
            raise TypeError(str(args[0]) + " is not <class int>")
        return int(
            ''.join(str(integer) for integer in (list(map(lambda x: 9 - x, list(int(y) for y in str(args[0])))))))


# ----------------------------------------------------------------------------------------------------------------------
##############################
#     Parsing Section        #
##############################

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree


def tokenize(line):
    """Convert a string into a list of tokens. """
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ').replace("'", "")
    return spaced.strip().split()


known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/', 'compl', '!', 'int']

# special dictionary that gets base and converts it into decimal representation
all_bases_to_decimal_dic = {'b': 2, 'q': 8, 'h': 16, }


def analyze(tokens):
    """
    Create a tree of nested lists from a sequence of tokens.
    Operand expressions can be separated by commas, spaces, or both.
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
        # condition that check whether an input is given with other base that aren't decimal base
    if token[len(token) - 1] in all_bases_to_decimal_dic.keys():
        temp_token = token[:len(token) - 1]

        if temp_token[0] == "'":
            temp_token = temp_token[1:]
            temp_token += 'b'
        temp_token = int(temp_token, all_bases_to_decimal_dic[token[len(token) - 1]])
        token = temp_token
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)


def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands


def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token."""
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


# ----------------------------------------------------------------------------------------------------------------------
def run():
    read_eval_print_loop()

# run()
