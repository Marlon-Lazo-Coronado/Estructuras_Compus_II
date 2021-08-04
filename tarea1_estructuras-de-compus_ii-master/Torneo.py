#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from Aux1 import Aux11
from Aux2 import Aux22


def predictor_4(s,ph,gh):
    tsi=0
    tno=0
    nsi=0
    nno=0
    hit=0
    miss=0
    i=0
    p=0

    EP=[]
    for x in range((2**s)):         # Tabla de contadores
        EP.append(0)

    ################################################################
    #state=0
    ghm = pow(2,gh)-1 # bits de historia
    Bits_estados = pow(2,s)-1 # bits de estados
    Xhistoria2 = ghm

    # Creamos el vector de estados y de direcciones
    GHT=[]
    GHT.append(ghm)

    BHT=[]
    for x in range((2**s)):         # Tabla de contadores
        BHT.append(0)
    ##################################################################
    historia=0
    Xhistoria=0
    state=0
    historia = pow(2,ph)-1   # bits de historia
    Xhistoria = historia

    BHT=[]
    PHT=[]
    for x in range((2**s)):
        PHT.append(historia)
        BHT.append(0)
    #####################################################################




    for line in sys.stdin:
        i =i+1


        bandera1=Aux11(state,s,line,Xhistoria,BHT,PHT)
        bandera2=Aux22(state,s,line,Xhistoria2,GHT,BHT,Bits_estados)

        temp = EP[p]


        if (temp == 0):
            if ((bandera1 == 0) & (bandera2 == 0)):
                EP[p]=0
                miss=miss+1
                nno=nno+1

            if ((bandera1 == 0) & (bandera2 == 1)):
                EP[p]=1
                miss=miss+1
                nno=nno+1

            if ((bandera1 == 1) & (bandera2 == 0)):
                EP[p]=0
                hit=hit+1
                nsi=nsi+1

            if ((bandera1 == 1) & (bandera2 == 1)):
                EP[p]=0
                hit=hit+1
                nsi=nsi+1

        if (temp == 1):

            if ((bandera1 == 0) & (bandera2 == 0)):
                EP[p]=1
                miss=miss+1
                nno=nno+1

            if ((bandera1 == 0) & (bandera2 == 1)):
                EP[p]=2
                miss=miss+1
                nno=nno+1

            if ((bandera1 == 1) & (bandera2 == 0)):
                EP[p]=0
                hit=hit+1
                nsi=nsi+1

            if ((bandera1 == 1) & (bandera2 == 1)):
                EP[p]=1
                hit=hit+1
                nsi=nsi+1

        if (temp == 2):

            if ((bandera1 == 0) & (bandera2 == 0)):
                EP[p]=2
                miss=miss+1
                tno=tno+1

            if ((bandera1 == 0) & (bandera2 == 1)):
                EP[p]=3
                hit=hit+1
                tsi=tsi+1

            if ((bandera1 == 1) & (bandera2 == 0)):
                EP[p]=1
                miss=miss+1
                tno=tno+1

            if ((bandera1 == 1) & (bandera2 == 1)):
                EP[p]=2
                hit=hit+1
                tsi=tsi+1

        if (temp == 3):

            if ((bandera1 == 0) & (bandera2 == 0)):
                EP[p]=3
                miss=miss+1
                tno=tno+1

            if ((bandera1 == 0) & (bandera2 == 1)):
                EP[p]=3
                hit=hit+1
                tsi=tsi+1

            if ((bandera1 == 1) & (bandera2 == 0)):
                EP[p]=2
                miss=miss+1
                tno=tno+1

            if ((bandera1 == 1) & (bandera2 == 1)):
                EP[p]=3
                hit=hit+1
                tsi=tsi+1


    print(miss)
    print(hit)
    print('\n*********************************************************')
    print('\nBranch prediction type:  \t\t\tBimodal')
    print('\nBHT size (entries):  \t\t\t\t', 2**s)
    print('\nGlobal history register size: \t\t\t', 2**gh)
    print('\nPrivate history register size: \t\t\t', 2**ph)
    print('***********************************************************')
    print('\nNumber of branch: \t\t\t\t', i)
    print('\nNumber of correct prediction of taken branches: ', tsi)
    print('\nNumber of incorrect prediction of taken branches: ', tno)
    print('\nCorrect prediction of not taken branches: ', nsi)
    print('\nIncorrect prediction of not taken branches: ', nno)
    print('\nPercentage of correct predictions: ', ((hit)/i)*100)
    print('\n**********************************************************\n')
