#
# Name: Lawrence Mao
# Date: 10-27-17
#

from binarizelib import *
                                                           # list your images e.g., trump.jpeg with threshold of 
"""
trump.jpg        thr: 140  | Donald Trump
clinton.jpg      thr: 130  | Hillary Clinton
"""

def clear():                                               # resets terminal with blank
    print('\n' * 200)

def fill():                                                # fills terminal with 'X' 
    for x in range(200):
        print('X' * 491)

def checkGrey(p):                                          # calculating luminescence
    red = p[0]
    green = p[1]
    blue = p[2]
    lum = int(.21 * red + .72 * green + .07 * blue)
    return lum

def binarize(*arg):                                        # main, takes in four inputs
    """ 
    in: img, thr, ch1, ch2
    """
    img = arg[0]
    thr = 127
    ch1 = 'xx'
    ch2 = '  '
    if len(arg) > 1:                                       # since *arg takes in infinite amount, nested if statements to control up to 4
        thr = arg[1]
        if len(arg) > 2:
            ch1 = 2*arg[2]
            if len(arg) > 3:
                ch2 = 2*arg[3]
                if len(arg) > 4:
                    print('The following inputs were ignored:')
                    for x in arg[4:-1]:
                        print(x)
    Im_pix = getRGB(img)                                 # get the image from user
    toPrint = []

    for row in Im_pix:                                      
        for p in row:
            if checkGrey(p) > thr:                         # appends 'xx'
                toPrint.append(ch1)
            else:                                          # appends '  '
                toPrint.append(ch2)
        toPrint.append('\n')                          
    for dot in toPrint:
        print(dot, end='')