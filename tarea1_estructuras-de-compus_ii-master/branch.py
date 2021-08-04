#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Estructuras de Computadores II
#Tarea 1
#Marlon Lazo Coronado
#Simulacion de predictores de saltos
'''import numpy as np'''
import sys
from sys import argv
from Contador_Bimodal import predictor_1
#Simulacion de predictores de saltos
from P_Historia_Pribada import predictor_2
from Global_Predictor import predictor_3
from Torneo import predictor_4

scrip, arg1,arg2,arg3,arg4=argv
s=int(arg1)
bp=int(arg2)
gh=int(arg3)
ph=int(arg4)


if bp==0:
    predictor_1(s)
elif bp==2:
    predictor_3(s,gh)
elif bp==1:
    predictor_2(s,ph)
elif bp==3:
    predictor_4(s,ph,gh)






'''> <'''
