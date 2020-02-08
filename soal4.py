# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:24:15 2020

@author: Players
"""
def kataganti(kataasal): 
    kalimatbaru = [] 
    listkata = list(kataasal) 
    for hurufganti in listkata: 
        if hurufganti == 'a': 
            kalimatbaru.append('u')
        elif hurufganti == 'b':
            kalimatbaru.append('m')
        elif hurufganti == 'c':
            kalimatbaru.append('c') 
        elif hurufganti == 'd':
            kalimatbaru.append('d')
        elif hurufganti == 'e':
            kalimatbaru.append('e')
        elif hurufganti == 'f':
            kalimatbaru.append('f')
        elif hurufganti == 'g':
            kalimatbaru.append('g')
        elif hurufganti == 'h':
            kalimatbaru.append('x')
        elif hurufganti == 'i':
            kalimatbaru.append('i')
        elif hurufganti == 'j':
            kalimatbaru.append('j')
        elif hurufganti == 'k':
            kalimatbaru.append('k')
        elif hurufganti == 'l':
            kalimatbaru.append('l')
        elif hurufganti == 'm':
            kalimatbaru.append('m')
        elif hurufganti == 'n':
            kalimatbaru.append('n')
        elif hurufganti == 'o':
            kalimatbaru.append('o')
        elif hurufganti == 'p':
            kalimatbaru.append('p')
        elif hurufganti == 'q':
            kalimatbaru.append('q')
        elif hurufganti == 'r':
            kalimatbaru.append('r')
        elif hurufganti == 's':
            kalimatbaru.append('s')
        elif hurufganti == 't':
            kalimatbaru.append('t')
        elif hurufganti == 'u':
            kalimatbaru.append('u')
        elif hurufganti == 'v':
            kalimatbaru.append('v')
        elif hurufganti == 'w':
            kalimatbaru.append('w')
        elif hurufganti == 'x':
            kalimatbaru.append('x')
        elif hurufganti == 'y':
            kalimatbaru.append('y')
        elif hurufganti == 'z':
            kalimatbaru.append('z')
        elif hurufganti == ' ':
            kalimatbaru.append(' ')
    return "".join(kalimatbaru)
print (kataganti("mari belajar python"))