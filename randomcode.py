# coding: utf-8
import random
import string
def rand_str(num,length = 7):
    for i in range(num):
        chars = string.letters + string.digits
        s = [random.choice(chars) for i in range(7)]
        print ''.join(s)

if __name__ == "__main__":
    rand_str(200)
