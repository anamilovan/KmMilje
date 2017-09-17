#!/usr/bin/env python
# -*- coding: utf-8 -*-

km = 0;
milje = 0;
pretvorba = "da";
print "Pozdravljeni! Sem program, ki pretvarja kilometre v milje."


while pretvorba.lower() == "da" :
    print "Ali zelis pretvoriti km v milje?"
    pretvorba = str(raw_input(""))

    if pretvorba.lower() == "da":
        km = float(int(raw_input("Vnesite stevilo kilometrov")))
        milje = km * 0.621371192
        print str(km) + " kilometorv je " + str(milje) + " milj."
    else:
        print "Hvala, da si uporabljal nas program!"