#!/usr/bin/env python

import sys


if len(sys.argv) != 2:
    print 'Usage: %s file.dat' % sys.argv[0]
    print 'Splits a 32K file.dat file into 32 1K track files 00.dat to 31.dat'
    sys.exit()



infile = open(sys.argv[1], 'rb')

track00file = open("00.dat", 'wb')
track01file = open("01.dat", 'wb')
track02file = open("02.dat", 'wb')
track03file = open("03.dat", 'wb')
track04file = open("04.dat", 'wb')
track05file = open("05.dat", 'wb')
track06file = open("06.dat", 'wb')
track07file = open("07.dat", 'wb')
track08file = open("08.dat", 'wb')
track09file = open("09.dat", 'wb')
track10file = open("10.dat", 'wb')
track11file = open("11.dat", 'wb')
track12file = open("12.dat", 'wb')
track13file = open("13.dat", 'wb')
track14file = open("14.dat", 'wb')
track15file = open("15.dat", 'wb')
track16file = open("16.dat", 'wb')
track17file = open("17.dat", 'wb')
track18file = open("18.dat", 'wb')
track19file = open("19.dat", 'wb')
track20file = open("20.dat", 'wb')
track21file = open("21.dat", 'wb')
track22file = open("22.dat", 'wb')
track23file = open("23.dat", 'wb')
track24file = open("24.dat", 'wb')
track25file = open("25.dat", 'wb')
track26file = open("26.dat", 'wb')
track27file = open("27.dat", 'wb')
track28file = open("28.dat", 'wb')
track29file = open("29.dat", 'wb')
track30file = open("30.dat", 'wb')
track31file = open("31.dat", 'wb')

t00dat = infile.read(1024)
t01dat = infile.read(1024)
t02dat = infile.read(1024)
t03dat = infile.read(1024)
t04dat = infile.read(1024)
t05dat = infile.read(1024)
t06dat = infile.read(1024)
t07dat = infile.read(1024)
t08dat = infile.read(1024)
t09dat = infile.read(1024)
t10dat = infile.read(1024)
t11dat = infile.read(1024)
t12dat = infile.read(1024)
t13dat = infile.read(1024)
t14dat = infile.read(1024)
t15dat = infile.read(1024)
t16dat = infile.read(1024)
t17dat = infile.read(1024)
t18dat = infile.read(1024)
t19dat = infile.read(1024)
t20dat = infile.read(1024)
t21dat = infile.read(1024)
t22dat = infile.read(1024)
t23dat = infile.read(1024)
t24dat = infile.read(1024)
t25dat = infile.read(1024)
t26dat = infile.read(1024)
t27dat = infile.read(1024)
t28dat = infile.read(1024)
t29dat = infile.read(1024)
t30dat = infile.read(1024)
t31dat = infile.read(1024)

track00file.write(t00dat)
track01file.write(t01dat)
track02file.write(t02dat)
track03file.write(t03dat)
track04file.write(t04dat)
track05file.write(t05dat)
track06file.write(t06dat)
track07file.write(t07dat)
track08file.write(t08dat)
track09file.write(t09dat)
track10file.write(t10dat)
track11file.write(t11dat)
track12file.write(t12dat)
track13file.write(t13dat)
track14file.write(t14dat)
track15file.write(t15dat)
track16file.write(t16dat)
track17file.write(t17dat)
track18file.write(t18dat)
track19file.write(t19dat)
track20file.write(t20dat)
track21file.write(t21dat)
track22file.write(t22dat)
track23file.write(t23dat)
track24file.write(t24dat)
track25file.write(t25dat)
track26file.write(t26dat)
track27file.write(t27dat)
track28file.write(t28dat)
track29file.write(t29dat)
track30file.write(t30dat)
track31file.write(t31dat)

track00file.close()
track01file.close()
track02file.close()
track03file.close()
track04file.close()
track05file.close()
track06file.close()
track07file.close()
track08file.close()
track09file.close()
track10file.close()
track11file.close()
track12file.close()
track13file.close()
track14file.close()
track15file.close()
track16file.close()
track17file.close()
track18file.close()
track19file.close()
track20file.close()
track21file.close()
track22file.close()
track23file.close()
track24file.close()
track25file.close()
track26file.close()
track27file.close()
track28file.close()
track29file.close()
track30file.close()
track31file.close()