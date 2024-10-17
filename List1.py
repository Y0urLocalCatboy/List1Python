import math
from math import floor
from random import randint
import matplotlib.pyplot as plt


def weekday(day, month, year):
    """
    This function takes the date and returns the day of the week

    Parameters:
        day(int): which day
        month(int): which month
        year(int): which year
    Returns:
        dayZero(int): The day of the week
    """
    yearZero = year - floor((14 - month)/12)
    x = yearZero + floor(yearZero/4) - floor(yearZero/100) + floor(yearZero/400)
    monthZero = month + 12 * floor((14 - month)/12) - 2
    dayZero = (day + x + floor(31 * monthZero / 12)) % 7
    return dayZero
print(weekday(4, 8, 2009))

def segment_length(Ap, Ak, Bp, Bk):
    """
    This function takes the coordinates of twi line segments in a one dimensional space and calculates the intersection between them

    Parameters:
        Ap(int): the beginning of segment A
        Ak(int): the end of segment A
        Bp(int): the beginning of segment B
        Bk(int): the end of segment B
    Returns:
        intersection(String): the intersection
    """
    if Ap > Ak:
        Ap, Ak = Ak, Ap
    if Bp > Bk:
        Bp, Bk = Bk, Bp
    if Ap > Bk or Bp > Ak:
        return "None"
    if Ap == Bk or Bp == Ak:
        return "Just a point"
    if Ak > Bp:
        return "(%d, %d)" %(Bp, Ak)
    if Bk > Bp:
        return "(%d, %d)" %(Ap, Bk)
    pass
print(segment_length(1, 2, 2, 7))


def random_walk(n):
    """
    This function simulates a random walk in a 2D space and stops when is n units away from the centre
    Parameters:
        n(int): the limit of the walk
    Returns:
        steps(list): the steps of the walk
    """
    steps = []
    x = 0 #coordinate x
    y = 0 #coordinate y
    while n >= math.sqrt(x** 2 + y** 2):
        direction = randint(0, 3)
        if direction == 0:
            x += 1
        elif direction == 1:
            x -= 1
        elif direction == 2:
            y += 1
        else:
            y -= 1
        steps.append((x, y))
    return steps
def plot_walk():
    """
    This function plots the walk using random_walk
    Parameters:
        None
    Returns:
        None
    """
    n = 100
    coordinates = random_walk(100)
    x, y = zip(*coordinates)
    plt.plot(x, y, marker='o', linestyle='-', markersize=2)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Walker\'s Trajectory')
    plt.grid(True)
    plt.show()
plot_walk()

def dec2bin(x):
    """
    This function converts a decimal number to its binary counterpanrt
    Parameters:
        x(int): the decimal number
    Returns:
        binary(str): the binary number
    """
    i=1
    binary=""
    operations = ""
    is_negative = False
    if x==0:
        return "0"
    if x<0:
        x = abs(x)
        is_negative = True
    while x >= 1:
        binary = str(x % 2) + binary
        operations = operations + "%d. %d divided by 2. Quotient: %d, Remainder: %d \n" %(i, x, x//2, x%2)
        x = x//2
        i+=1
    print(operations)
    if is_negative:
        return "-" + binary
    return binary
print(dec2bin(-2))

def dna_complement(orig_strand):
    """
    This function takes a DNA strand and returns its complement using the Watson-Crick pairing rules
    Parameters:
        orig_strand(str): the original DNA strand
    Returns:
        complement(str): the complement DNA strand
    """
    complement = ""
    for i in orig_strand:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
        else:
            return "Invalid DNA strand"
    return complement