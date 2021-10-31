# ==============================================================================
"""A solution to the traditional programming puzzle called FizzBuzz"""

def fizz_buzz(num):
    """Play FizzBuzz up to the number `num`"""
    for i in range(1, num+1):
        flag = True
        if i % 5 == 0:
            print("Fizz", end="")
            flag = False
        if i % 3 == 0:
            print("Buzz", end="")
            flag = False

        if flag:
            print(i)
        else:
            print()

fizz_buzz(20)
