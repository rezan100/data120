#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:46:22 2021

@author: rezanmoustafa
"""

# Endret fra 8b til 9
class Sporsmaal:
    def __init__(self, sporsmaal, svar, valg=[]):
        self.sporsmaal=sporsmaal
        self.svar=svar
        self.valg=valg
   
    def HentSporsmaal(self):
        print(self.sporsmaal)
        for i in range(len(self.valg)):
            print(i, self.valg[i])
    # Deloppgave 9e)
    def korrekt_svar_tekst(self):
        return self.valg[self.svar]

# Deloppgave 9d)
def les_filen(sporsmaalsfil):
    sporsmaalene = []
    file = open('sporsmaalsfil.txt','r')
    for line in file:
        line = line.strip().split(':')
        sporsmaal = line[0];
        svar = int(line[1])
        lst = []
        for val in line[2].split(","):
            lst.append(val)
        sporsmaalene.append(Sporsmaal(sporsmaal,svar,lst))
    file.close()
    return sporsmaalene

# Deloppgave 9f)
if __name__=="__main__":
    sporsmaalene = les_filen("sporsmaalsfil.txt")
    spiller1Score = 0
    spiller2Score = 0
    for i in range(len(sporsmaalene)):
        sporsmaalene[i].HentSporsmaal()
        spiller1 = int(input('\nSpiller 1: '))
        spiller2 = int(input('Spiller 2: '))
        print("\nRiktig svar: ",sporsmaalene[i].korrekt_svar_tekst())
        if spiller1 == sporsmaalene[i].svar:
            spiller1Score += 1
        if spiller2 == sporsmaalene[i].svar:
            spiller2Score += 1
        print()
    print("\nSpiller 1 har ",spiller1Score,' av ',len(sporsmaalene))
    print("Spiller 2 har ",spiller2Score,' av ',len(sporsmaalene))
    if spiller1Score > spiller2Score:
        print("\nSpiller 1 er vinneren!!!")
    elif spiller2Score > spiller1Score:
        print("\nSpiller 2 er vinneren!!!")
    else:
        print("\nDet ble uavgjort!!!")
      