#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def predictor_3(a,historia):
    Phistoria=historia
    tsi=0
    tno=0
    nsi=0
    nno=0
    state=0
    miss=0
    hit=0
    historia = pow(2,historia)-1 # bits de historia
    Bits_estados = pow(2,a)-1 # bits de estados
    Xhistoria = historia
    i=0
    # Creamos el vector de estados y de direcciones
    PHT=[]
    PHT.append(historia)

    BHT=[]
    for x in range((2**a)):         # Tabla de contadores
        BHT.append(0)
    #print(C)
    #len(C)


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

        historia = PHT[0]
        #print(historia)
        direccion = historia ^ p
        if Bits_estados < Xhistoria:
            direccion = Bits_estados & direccion
        temp=BHT[direccion]
        state=BHT[direccion]
        # Si tienemos 12 espacios en la linea
        if line[10] == " ":                      # Saltos no tomados
            if ((temp == 0) & (line[11]=="N")):
                hit = hit + 1
                # Hacer el desplazamiento
                PHT[0] = ((historia << 1) & (Xhistoria))
                nsi=nsi+1


            if ((temp == 1) & (line[11]=="N")):
                hit = hit + 1
                state = state - 1
                BHT[direccion] = state
                PHT[0] = ((historia << 1) & (Xhistoria))
                nsi=nsi+1

            if ((temp == 2) & (line[11]=="N")):
                miss = miss + 1
                state = state - 1
                BHT[direccion] = state
                PHT[0] = ((historia << 1) & (Xhistoria))
                tno=tno+1

            if ((temp == 3) & (line[11]=="N")):
                miss = miss +1
                state = state - 1
                BHT[direccion] = state
                PHT[0] = ((historia << 1) & (Xhistoria))
                tno=tno+1

            # Saltos tomados
            if ((temp == 0) & (line[11]=="T")):
                miss = miss +1
                state = state + 1
                BHT[direccion] = state
                PHT[0] = (((historia << 1) & (Xhistoria)) | 1)
                nno=nno+1

            if ((temp == 1) & (line[11]=="T")):
                miss = miss +1
                state = state + 1
                BHT[direccion] = state
                PHT[0] = (((historia << 1) & (Xhistoria)) | 1)
                nno=nno+1

            if ((temp == 2) & (line[11]=="T")):
                hit = hit +1
                state = state + 1
                BHT[direccion] = state
                PHT[0] = (((historia << 1) & (Xhistoria)) | 1)
                tsi=tsi+1

            if ((temp == 3) & (line[11]=="T")):
                hit = hit + 1
                PHT[0] = (((historia << 1) & (Xhistoria)) | 1)
                tsi=tsi+1


        # Si tienemos 12 espacios en la linea
        else:                                   # Saltos no tomados
            if ((temp == 0) & (line[10]=="N")):
                hit = hit + 1
                PHT[0] = ((historia << 1) & (Xhistoria))
                nsi=nsi+1

            if ((temp == 1) & (line[10]=="N")):
                hit = hit + 1
                state = state - 1
                BHT[direccion] = state
                PHT[0] = ((historia << 1) & (Xhistoria))
                nsi=nsi+1

            if ((temp == 2) & (line[10]=="N")):
                miss = miss + 1
                state = state - 1
                BHT[direccion] = state
                PHT[0] = ((historia << 1) & (Xhistoria))
                tno=tno+1

            if ((temp == 3) & (line[10]=="N")):
                miss = miss +1
                state = state - 1
                BHT[direccion] = state
                PHT[0] = ((historia << 1) & (Xhistoria))
                tno=tno+1

            # Saltos tomados
            if ((temp == 0) & (line[10]=="T")):
                miss = miss +1
                state = state + 1
                BHT[direccion] = state
                PHT[0] = (((historia << 1) & (Xhistoria)) | 1)
                nno=nno+1

            if ((temp == 1) & (line[10]=="T")):
                miss = miss +1
                state = state + 1
                BHT[direccion] = state
                PHT[0] = (((historia << 1) & (Xhistoria)) | 1)
                nno=nno+1

            if ((temp == 2) & (line[10]=="T")):
                hit = hit +1
                state = state + 1
                BHT[direccion] = state
                PHT[0] = (((historia << 1) & (Xhistoria)) | 1)
                tsi=tsi+1

            if ((temp == 3) & (line[10]=="T")):
                hit = hit +1
                PHT[0] = (((historia << 1) & (Xhistoria)) | 1)
                tsi=tsi+1



        '''
        print(t)
        print(bin(t))
        print(bin(a))
        print(bin(p))'''

    print(miss)
    print(hit)
    print('\n*********************************************************')
    print('\nBranch prediction type:  \t\t\tHistoria Global')
    print('\nBHT size (entries):  \t\t\t\t', 2**a)
    print('\nGlobal history register size: \t\t\t', 2**Phistoria)
    print('\nPrivate history register size: \t\t\t', 0)
    print('***********************************************************')
    print('\nNumber of branch: \t\t\t\t', i)
    print('\nNumber of correct prediction of taken branches: ', tsi)
    print('\nNumber of incorrect prediction of taken branches: ', tno)
    print('\nCorrect prediction of not taken branches: ', nsi)
    print('\nIncorrect prediction of not taken branches: ', nno)
    print('\nPercentage of correct predictions: ', ((hit)/i)*100)
    print('\n**********************************************************\n')
