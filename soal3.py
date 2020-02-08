# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:02:26 2020

@author: Players
"""

def hitung_vokal(kata, vokal):
    kata = kata.lower()
    jumlah = {}.fromkeys(vokal, 0)
    for vokal in kata :
        if vokal in jumlah :
            jumlah[vokal]+=1
    return jumlah
vokal = "aiueo"
kata = "belajar coding di Arkademy itu menyenangkan"
print (hitung_vokal(kata, vokal))