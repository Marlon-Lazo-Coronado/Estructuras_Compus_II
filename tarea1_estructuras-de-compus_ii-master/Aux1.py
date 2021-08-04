#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def Aux11(state,a,line,Xhistoria,BHT,PHT):
    bandera=0

    #print(C)
    #len(C)

    paso=0

    if paso==0:
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

        historia = PHT[p]
        #print(historia)
        direccion = historia ^ p
        temp=BHT[direccion]
        state=BHT[direccion]
        # Si tienemos 12 espacios en la linea
        if line[10] == " ":                      # Saltos no tomados
            if ((temp == 0) & (line[11]=="N")):
                # Hacer el desplazamiento
                PHT[p] = ((historia << 1) & (Xhistoria))
                bandera=1

            if ((temp == 1) & (line[11]=="N")):
                state = state - 1
                BHT[direccion] = state
                PHT[p] = ((historia << 1) & (Xhistoria))
                bandera=1

            if ((temp == 2) & (line[11]=="N")):
                state = state - 1
                BHT[direccion] = state
                PHT[p] = ((historia << 1) & (Xhistoria))
                bandera=0

            if ((temp == 3) & (line[11]=="N")):
                state = state - 1
                BHT[direccion] = state
                PHT[p] = ((historia << 1) & (Xhistoria))
                bandera=0

            # Saltos tomados
            if ((temp == 0) & (line[11]=="T")):
                state = state + 1
                BHT[direccion] = state
                PHT[p] = (((historia << 1) & (Xhistoria)) | 1)
                bandera=0

            if ((temp == 1) & (line[11]=="T")):
                state = state + 1
                BHT[direccion] = state
                PHT[p] = (((historia << 1) & (Xhistoria)) | 1)
                bandera=0

            if ((temp == 2) & (line[11]=="T")):
                state = state + 1
                BHT[direccion] = state
                PHT[p] = (((historia << 1) & (Xhistoria)) | 1)
                bandera=1

            if ((temp == 3) & (line[11]=="T")):
                PHT[p] = (((historia << 1) & (Xhistoria)) | 1)
                bandera=1


        # Si tienemos 12 espacios en la linea
        else:                                   # Saltos no tomados
            if ((temp == 0) & (line[10]=="N")):
                PHT[p] = ((historia << 1) & (Xhistoria))
                bandera=1

            if ((temp == 1) & (line[10]=="N")):
                state = state - 1
                BHT[direccion] = state
                PHT[p] = ((historia << 1) & (Xhistoria))
                bandera=1

            if ((temp == 2) & (line[10]=="N")):
                state = state - 1
                BHT[direccion] = state
                PHT[p] = ((historia << 1) & (Xhistoria))
                bandera=0

            if ((temp == 3) & (line[10]=="N")):
                state = state - 1
                BHT[direccion] = state
                PHT[p] = ((historia << 1) & (Xhistoria))
                bandera=0

            # Saltos tomados
            if ((temp == 0) & (line[10]=="T")):
                state = state + 1
                BHT[direccion] = state
                PHT[p] = (((historia << 1) & (Xhistoria)) | 1)
                bandera=0

            if ((temp == 1) & (line[10]=="T")):
                state = state + 1
                BHT[direccion] = state
                PHT[p] = (((historia << 1) & (Xhistoria)) | 1)
                bandera=0

            if ((temp == 2) & (line[10]=="T")):
                state = state + 1
                BHT[direccion] = state
                PHT[p] = (((historia << 1) & (Xhistoria)) | 1)
                bandera=1

            if ((temp == 3) & (line[10]=="T")):
                PHT[p] = (((historia << 1) & (Xhistoria)) | 1)
                bandera=1

    return bandera
