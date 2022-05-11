# https://pynative.com/python-basic-exercise-for-beginners/

# 1. Given two integer numbers return their product only if the product is greater than 1000, else return their sum.


def productGrtr(number1, number2):
    product = number1 * number2
    if (product <= 1000):
        return product
    else:
        return number1 + number2

#1st condition
print("1st, ", productGrtr(20,30))
#2nd condition
print("2nd, ", productGrtr(20,30))


