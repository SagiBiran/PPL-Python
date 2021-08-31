import random
from functools import reduce
from math import sqrt
import string
from operator import add

"""
Assignment 3
Author: Sagi Biran
ID: 205620859
"""


# ------------------------------------------------
#                       Q#1
# ------------------------------------------------
def make_power(b, p):
    """Return a dispatch function that represents an exponential number."""

    def dispatch(i):
        """
        dispatch function will respond to index ,
        due index will return base or power that
        belong to the exponential number
        :param i: index to get base or power of exponential number
        :return: power or base belongs to that number
        """
        if i == 0:
            return b
        elif i == 1:
            return p

    return dispatch


def base(Base):
    """function will return the Base of exponentially number"""
    return Base(0)


def power(Power):
    """function will return the Power of exponentially number"""
    return Power(1)


def print_power(num):
    """
    function will prints a number's in exponential form due the parameter
    :param num: number to be printed in exponential form
    :return: exponential number
    """
    secondBase = {2: make_power(2, 1), 4: make_power(2, 2), 8: make_power(2, 3), 16: make_power(2, 4),
                  32: make_power(2, 5),
                  64: make_power(2, 6), 128: make_power(2, 7), 256: make_power(2, 8), 512: make_power(2, 9),
                  1024: make_power(2, 10), 2048: make_power(2, 11), 4096: make_power(2, 12), 8192: make_power(2, 13)}
    if callable(num):
        if base(num) == 0:
            print(0)
            return
        if base(num) == 1 or power(num) == 0:
            print(1)
            return
        if power(num) == 1:
            print(base(num))
            return
        print(f'{base(num)}^{power(num)}')
    elif num in secondBase:
        newNum = secondBase[num]
        print(f'{base(newNum)}^{power(newNum)}')
    else:
        print(num)


def is_square(n):
    """
    helper function will return True whether a number has a square otherwise return False
    :param n: number to be checked
    :return: whether a number has a square root or not.
    """
    return sqrt(n).is_integer()


def improve_power(num):
    """
    function will check whether the number in the parameter could be shrink or not
    the shrink will be operate by decrease the base and increase the power
    of exponential number
    :param num: exponential number
    :return: most efficient representation of exponential number
    """
    if base(num) < 0:
        return "Base for a number is negative , please check it.."
    elif base(num) == 0:
        return 0
    elif base(num) == 1:
        return 1
    elif is_square(base(num)):
        return make_power(int(sqrt(base(num))), power(num) * 2)
    else:
        return num


def calc_power(a, b):
    """
    calculate a return exponential number in integer representation
    :param a: base of exponential number
    :param b: power of exponential number
    :return: integer representation of exponential number
    """
    if b == 0:
        return 1

    answer = a
    increment = a

    for i in range(1, b):
        for j in range(1, a):
            answer += increment
        increment = answer
    return answer


def mul_power(num1, num2):
    """function will do multiplication between two numbers"""
    if base(num1) == base(num2):
        return make_power(base(num1), power(num1) + power(num2))
    else:
        return calc_power(base(num1), power(num1)) * calc_power(base(num2), power(num2))


def div_power(num1, num2):
    """function will do division between two numbers"""
    if not callable(num1):
        if not callable(num2):
            return int(num1 / num2)
        else:
            return int(num1 / calc_power(base(num2), power(num2)))
    else:
        if not callable(num2):
            return int(calc_power(base(num1), power(num1)) / num2)
        return make_power(base(num1), power(num1) - power(num2))


# ------------------------------------------------
#                       Q#2
# ------------------------------------------------
def value(tree):
    """
    return numerical result
    :param tree: binary tree representation
    :return: value in node
    """
    return tree(0)


def left(tree):
    """
    :param tree: binary tree
    :return: left son of node
    """
    return tree(1)


def right(tree):
    """
    :param tree: binary tree
    :return: right son of binary tree
    """
    return tree(2)


def make_tree(val, f, r):
    """
    immutable type that represent binary tree that has value and sons (right and left)
    the representation is included data abstraction and implement API by different abstraction layers
    :param val: value of given node
    :param f: first element (left son recursively)
    :param r: rest of list  (right son recursively)
    :return: binary tree immutable data type
    """

    def dispatch(i):
        """
        function will return value , left son / right son of given node.
        :param i: index for given element
        :return: desired element
        """
        if i == 0:
            return val
        elif i == 1:
            return f
        elif i == 2:
            return r

    return dispatch


def print_tree(tree):
    """
    :param tree: binary tree
    :return: printed tree by "Inorder" method
    """
    if callable(tree):
        print_tree(left(tree))
        print(value(tree), end=" ")
        print_tree(right(tree))


def count_value(tree, val):
    """
    :param tree: binary tree
    :param val: value to be searched over the tree
    :return: the number of occurrences that value showed in the tree
    """
    if tree is None:
        return 0
    count = 0
    if val == value(tree):
        count = 1
    count += count_value(left(tree), val)
    count += count_value(right(tree), val)
    return count


def tree_BST(tree):
    """
    :param tree: binary tree representation
    :return:  True whether the binary tree is BST else, return False
    """
    if tree is None or (left(tree) is None and right(tree) is None):
        return True
    elif right(tree) is None:
        return value(left(tree)) < value(tree) and tree_BST(left(tree))
    elif left(tree) is None:
        return value(right(tree)) >= value(tree) and tree_BST(right(tree))
    return tree_BST(left(tree)) and tree_BST(right(tree))


def tree_depth(tree):
    """
    :param tree: binary tree representation
    :return: the depth of given tree
    """
    depth = -1
    if left(tree):
        depth = max(depth, tree_depth(left(tree)))
    if right(tree):
        depth = max(depth, tree_depth(left(tree)))
    return depth + 1


def height(tree):
    """
    :param tree: binary tree representation
    :return: the height of given tree
    """
    # base condition when binary tree is empty
    if tree is None:
        return 0
    return max(height(left(tree)), height(right(tree))) + 1


def tree_balanced(tree):
    """
    :param tree: binary tree representation
    :return: True whether given tree is balanced tree else, return False
    """
    # Base condition
    if tree is None:
        return True

    # for left and right subtree height
    lh = height(left(tree))
    rh = height(right(tree))

    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and tree_balanced(left(tree)) is True and tree_balanced(right(tree)) is True:
        return True

    # if we reach here means tree is not
    # height-balanced tree
    return False


tree1 = make_tree(12, make_tree(6, make_tree(8, None, None), None),
                  make_tree(7, make_tree(8, None, None), make_tree(15, None, None)))
tree2 = make_tree(12, make_tree(6, make_tree(3, make_tree(1, None, None), None),
                                make_tree(8, make_tree(7, None, None), None)),
                  make_tree(15, None, make_tree(20, make_tree(17, None, None), None)))


# print(tree1)
# print(tree2)r
# print(value(tree1))
# print(value(left(tree1)))
# print(value(right(left(tree2))))
# print_tree(tree1)
# print()
# print_tree(tree2)
# print(count_value(tree1, 8))
# print(tree_BST(tree1))
# print(tree_BST(tree2))
# print(tree_depth(tree1))
# print(tree_depth(tree2))
# print(tree_balanced(tree1))
# print(tree_balanced(tree2))


# ------------------------------------------------
#                       Q#3
# ------------------------------------------------
def get_prices(storeName, Products, Sales):
    """Generator Expressions that return list of product with final prices (after calculated discounts)
    for specific store"""
    return tuple((pName, price * (1 - discount)) for pName, price in Products for sName, discount in
                 Sales if sName is storeName)


products = (('p1', 1000), ('p2', 2000), ('p3', 5000), ('p4', 100))
sales = (('s1', 0.2), ('s2', 0.3), ('s3', 0.1))


# print(get_prices('s1', products, sales))

def get_prices_dict(storeName, Products, Sales):
    """Generator Expressions that return product dictionary with final prices
    (after calculated discounts) for specific store"""
    return dict((pName, price * (1 - discount)) for pName, price in Products.items() for sName, discount in
                Sales.items() if sName is storeName)


prod_dict = dict(products)
sale_dict = dict(sales)


# print(get_prices_dict('s1', prod_dict, sale_dict))

def get_prices_by_type(storeName, Products, Sales, Types):
    """Generator Expressions that return dictionary of a products with final prices
    for specific store"""
    return dict(
        (product, price * (1 - theTypes[specificType])) for theStoreName, theTypes in Sales.items() if
        theStoreName == storeName for product, price in Products.items()
        for specificType, prodcts in Types.items()
        if product in prodcts
    )


sales = {'s1': {'t1': 0.2, 't2': 0.1}, 's2': {'t1': 0.1, 't2': 0.2}, 's3': {'t1': 0.3, 't2': 0.5}}
types = {'t1': ('p2', 'p4'), 't2': ('p1', 'p3')}


# print(get_prices_by_type('s1', prod_dict, sales, types))


def accumulate_prices(storeName, Products, Sales, Types, additionFunc):
    """Generator Expressions that return accumulated final prices (after calculated discounts)
    for all the products in given store"""
    return float(reduce(additionFunc, (get_prices_by_type(storeName, Products, Sales, Types)).values()))


# print(accumulate_prices('s1', prod_dict, sales, types, add))
# ------------------------------------------------
#                       Q#4
# ------------------------------------------------
def coding():
    """
    mutable type that allow the decode and encode text that composed by only
    words that separated by ONE space in message passing, dispatch functions method.
    :return: mutable type that can encode and decode given text
    """
    codingKey = {'reverse_word': False, 'reverse_string': False}
    originalSTR = ''
    encodeSTR = ''

    def rightRotate(givenList, number):
        """
        helper function that does rotation of given list (right rotation)
        :param givenList: of keys
        :param number: num that operated times of right rotation
        :return: rotated desired list
        """
        output_list = []
        # Will add values from n to the new list
        for tItem in range(len(givenList) - number, len(givenList)):
            output_list.append(givenList[tItem])
        # Will add the values before
        # n to the end of new list
        for tItem in range(0, len(givenList) - number):
            output_list.append(givenList[tItem])

        return output_list

    def left_rotate(givenList, number):

        """
        helper function that does rotation of given list (left rotation)
        :param givenList: of keys
        :param number: num that operated times of right rotation
        :return: rotated desired list
        """
        # arr - array to rotate
        # n - n number of rotations
        # For number of rotations greater than length of array
        number = number % len(givenList)
        return givenList[number:] + givenList[:number]

    def dispatch(msg, parameters=None):
        """
        :param msg: Message given by user to operate desired function
        :param parameters: parameters given by user to operate manipulation
        on given text , parameters is defined as DEFAULT PARAMETER
        :return: Desired function that respond to given message by user
        """
        nonlocal originalSTR
        nonlocal encodeSTR
        if msg == 'set_key':
            """
            make encrypted key by getting integer that decide left or right rotation of text
            by the sign of the number (with getting zero , user gets random rotation)
            """
            abcDict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i',
                       'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r',
                       's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
            if parameters[1] == 'yes':
                codingKey['reverse_word'] = True
            if parameters[2] == 'yes':
                codingKey['reverse_string'] = True
            abcDictValues = list(abcDict.values())
            if parameters[0] < 0:
                abcDictValues = rightRotate(abcDictValues, abs(parameters[0]))
            elif parameters[0] > 0:
                abcDictValues = left_rotate(abcDictValues, parameters[0])
            # user request 0 shifts then system will operate random shifting
            else:
                abcDictValues = rightRotate(abcDictValues, random.randint(1, 26))
            i = 0
            for item in abcDict:
                abcDict[item] = abcDictValues[i]
                i += 1
            codingKey.update(abcDict)
            return f'done'

        elif msg == 'export_key':
            """
            export encrypted key
            """
            if originalSTR == 'key empty':
                return print(f"'{originalSTR}'")
            return codingKey
        elif msg == 'encoding':
            """
            encoding operation on given text
            """
            originalSTR = parameters
            if codingKey['reverse_word'] is True and codingKey['reverse_string'] is True:
                tL = parameters.split()
                tL = ' '.join(tL)
                tL = tL[-1::-1]
                tL = tL.split()
                for word in tL:
                    for char in word:
                        if char in codingKey.keys():
                            char = codingKey[char]
                            encodeSTR += char
                    encodeSTR += ' '
                encodeSTR = encodeSTR[0:len(encodeSTR) - 1]
                return f'{encodeSTR}'
            elif codingKey['reverse_word'] is True and codingKey['reverse_string'] is False:
                tL = parameters.split(' ')
                tL1 = ' '.join(reversed(tL))
                encodeSTR = tL1
                return f'{encodeSTR}'
            elif codingKey['reverse_word'] is False and codingKey['reverse_string'] is True:
                tL = parameters.split(" ")
                tL1 = [word[::-1] for word in tL]
                tL2 = " ".join(tL1)
                encodeSTR = tL2
                return f'{encodeSTR}'
            else:
                encodeSTR = parameters
                return f'{encodeSTR}'
        elif msg == 'decoding':
            """
            decoding text operation
            """
            if originalSTR == 'Not Empty Key':
                inv_map = {v: k for k, v in codingKey.items()}
                tL = parameters.split()
                tL = ' '.join(tL)
                tL = tL[-1::-1]
                tL = tL.split()
                for word in tL:
                    for char in word:
                        if char in inv_map.keys():
                            char = inv_map[char]
                            encodeSTR += char
                    encodeSTR += ' '
                encodeSTR = encodeSTR[0:len(encodeSTR) - 1]
                return f'{encodeSTR}'
            elif originalSTR:
                return f'{originalSTR}'
            else:
                return f'key empty'
        elif msg == 'import_key':
            """
            import encrypted key
            """
            var = dispatch('set_key', (-3, 'yes', 'yes'))
            print(f"'{var}'")
            originalSTR = 'Not Empty Key'
        elif msg == 'empty_key':
            originalSTR = 'key empty'
            print(f"'done'")

    return dispatch


# code1 = coding()
# print(code1('set_key', (-3, 'yes', 'yes')))
# key = code1('export_key')
# print(key)
# cstr = code1('encoding', 'the london is the capital of great britain')
# print(cstr)
# dstr = code1('decoding', cstr)
# print(dstr)
# code2 = coding()
# dstr = code2('decoding', cstr)
# print(dstr)
# code2('import_key', key)
# dstr = code2('decoding', cstr)
# print(dstr)
# code2('empty_key')
# code2('export_key')

# ------------------------------------------------
#                       Q#5
# ------------------------------------------------
def parking(pHour, regularCapacity, priorityCapacity, vipCapacity):
    """Return a dispatch function that represents a bank account."""
    paymentPerHour = pHour
    parkingCapacity = {'Regular': regularCapacity, 'Priority': priorityCapacity,
                       'VIP': vipCapacity}
    parkingDetails = {'Regular': [], 'Priority': [], 'VIP': []}
    flag = False

    def print_list():
        """
        :return: function will print details of all cars located in parking
        """
        return {'end': end, 'next': next}

    def next():
        """
        :return: all cars in parking.
        """
        nonlocal flag
        for parkingType, cars in parkingDetails.items():
            if len(cars) != 0:
                for car in cars:
                    print(f'car: {car[0]}, parking type: {str(car[1])}, parking time: {car[2]}')
        flag = True

    def end():
        """
        :return: whether all cars in parking have been checked or not.
        """
        if flag:
            return True
        else:
            return False

    def print_parking(parkingType):
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

    def start_parking(carNumber, parkingType):
        """
        :param carNumber: car number that entering into parking
        :param parkingType: Type of entered car
        :return: a car entrance in parking
        """
        for carType in parkingDetails.keys():
            if parkingType == carType:
                if parkingCapacity[carType] == 0:
                    return print(f'{carType} parking is full')
                else:
                    parkingDetails[carType].append([carNumber, parkingType, 1])
                    parkingCapacity[carType] -= 1
                break

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


# park1 = parking(10, 3, 3, 3)
# print(park1)
# park1['start_parking'](222, 'Regular')
# park1['start_parking'](223, 'Regular')
# park1['next_time']()
# park1['start_parking'](224, 'Regular')
# park1['start_parking'](225, 'Regular')
# park1['start_parking'](225, 'VIP')
# prn = park1['print_list']()
# print(prn)
# while not prn['end']():
#     prn['next']()
# park1['print_parking']('VIP')
# park1['end_parking'](100)
# park1['end_parking'](223)
# park1['print_parking']('Regular')

