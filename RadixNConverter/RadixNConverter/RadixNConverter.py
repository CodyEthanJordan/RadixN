from scipy.special import lambertw
import numpy as np

def largestDigit(x):
    approx = np.real(np.exp(lambertw(np.log(x))))
    return int(np.floor(approx))

def digitConverter(val):
    '''Converts a base-10 representation of a single digit to a radixN digit,
    following the standard convention of
    0-9, a-z, A-Z, top of the keyboard, Unicode rainbow'''
    if val < 10:
        return str(int(val))
    elif val < 36: # the a through z sequence
        letterIndex = val - 10
        return chr(ord('a') + letterIndex)
    elif val < 62: # the A through Z sequence
        letterIndex = val - 36
        return chr(ord('A') + letterIndex)
    elif val == 62:
        return '!'
    elif val == 63:
        return '@'
    elif val == 64:
        return '#'
    elif val == 65:
        return '$'
    elif val == 66:
        return '%'
    elif val == 67:
        return '^'
    elif val == 68:
        return '&'
    elif val == 69:
        return '*'
    elif val == 70:
        return '('
    elif val == 71:
        return ')'
    elif val == 72:
        return '_'
    elif val == 73:
        return '+'

def convert(x):
    '''Converts boring base 10 number x to a list of strings representation of its Radix N
    format.'''
    n = largestDigit(x)
    radixN = ['0'] * (n + 1) # Make room for the free space
    radixN[0] = '*'
    while (x > 0):
        n = largestDigit(x)
        val = np.floor(x / (n**n))
        radixN[n] = digitConverter(val)
        x = x - val * (n ** n)

    return list(reversed(radixN))

for i in range(1,100):
    print(str(i) + "   :     " + "".join(convert(i)))