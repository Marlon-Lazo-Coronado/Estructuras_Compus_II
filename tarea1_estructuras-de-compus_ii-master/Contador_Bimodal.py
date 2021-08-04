#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def predictor_1(a):
    tsi=0
    tno=0
    nsi=0
    nno=0
    state=0
    miss=0
    hit=0
    # Creamos el vector de estados y de direcciones
    b=0
    C=[]
    for x in range((2**a)):         # Tabla de contadores
        C.append(0)
    #print(C)
    #len(C)

    i=0
    for line in sys.stdin:
        i=i+1
        error = line[11]
        if error == " ":
            t=int(line[0:11])
        else:
            t=int(line[0:10])
        p = t & ((2**a)-1)  # Mascara para la direcion filtrad
        #print(bin(p))
        #print(p)
        #print(line)

        #Se plantean todos los posibles casos que se pueden dar cuando se toma el estados
        # y se hace dos veces porque algunas veces la linea tiene 9 0 10 digitos

        #Se manipula el vector de estados
        state = C[p]
        temp = C[p]
        # Si tienemos 12 espacios en la linea
        if line[10] == " ":                      # Saltos no tomados
            if ((temp == 0) & (line[11]=="N")):
                hit = hit + 1
                nsi=nsi+1

            if ((temp == 1) & (line[11]=="N")):
                hit = hit + 1
                state = state - 1
                C[p] = state
                nsi=nsi+1

            if ((temp == 2) & (line[11]=="N")):
                miss = miss + 1
                state = state - 1
                C[p] = state
                tno=tno+1

            if ((temp == 3) & (line[11]=="N")):
                miss = miss +1
                state = state - 1
                C[p] = state
                tno=tno+1

            # Saltos tomados
            if ((temp == 0) & (line[11]=="T")):
                miss = miss +1
                state = state + 1
                C[p] = state
                nno=nno+1

            if ((temp == 1) & (line[11]=="T")):
                miss = miss +1
                state = state + 1
                C[p] = state
                nno=nno+1

            if ((temp == 2) & (line[11]=="T")):
                hit = hit +1
                state = state + 1
                C[p] = state
                tsi=tsi+1

            if ((temp == 3) & (line[11]=="T")):
                hit = hit +1
                tsi=tsi+1



        # Si tienemos 12 espacios en la linea
        else:                                   # Saltos no tomados
            if ((temp == 0) & (line[10]=="N")):
                hit = hit + 1
                nsi=nsi+1

            if ((temp == 1) & (line[10]=="N")):
                hit = hit + 1
                state = state - 1
                C[p] = state
                nsi=nsi+1

            if ((temp == 2) & (line[10]=="N")):
                miss = miss + 1
                state = state - 1
                C[p] = state
                tno=tno+1

            if ((temp == 3) & (line[10]=="N")):
                miss = miss +1
                state = state - 1
                C[p] = state
                tno=tno+1

            # Saltos tomados
            if ((temp == 0) & (line[10]=="T")):
                miss = miss +1
                state = state + 1
                C[p] = state
                nno=nno+1

            if ((temp == 1) & (line[10]=="T")):
                miss = miss +1
                state = state + 1
                C[p] = state
                nno=nno+1

            if ((temp == 2) & (line[10]=="T")):
                hit = hit +1
                state = state + 1
                C[p] = state
                tsi=tsi+1

            if ((temp == 3) & (line[10]=="T")):
                hit = hit +1
                tsi=tsi+1




        '''
        print(t)
        print(bin(t))
        print(bin(a))
        print(bin(p))'''
        #if i==100000:
            #break #Para no correr todas las direcciones
    print(miss)
    print(hit)
    print('\n*********************************************************')
    print('\nBranch prediction type:  \t\t\tBimodal')
    print('\nBHT size (entries):  \t\t\t\t', 2**a)
    print('\nGlobal history register size: \t\t\t', 0)
    print('\nPrivate history register size: \t\t\t', 0)
    print('***********************************************************')
    print('\nNumber of branch: \t\t\t\t', i)
    print('\nNumber of correct prediction of taken branches: ', tsi)
    print('\nNumber of incorrect prediction of taken branches: ', tno)
    print('\nCorrect prediction of not taken branches: ', nsi)
    print('\nIncorrect prediction of not taken branches: ', nno)
    print('\nPercentage of correct predictions: ', ((hit)/i)*100)
    print('\n**********************************************************\n')
