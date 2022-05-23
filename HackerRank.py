#Python If-Else

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())


def ConditionalStatement (n):
    evenOrOdd = n%2
    if (evenOrOdd > 0):
        print("Weird")
    else:
        if(n >= 2 and n <= 5):
            print("Not Weird")
        elif (n>= 6 and n <= 20):
            print("Weird")
        elif (n >20):
            print("Not Weird")
        else:
            exit()

ConditionalStatement(n)
