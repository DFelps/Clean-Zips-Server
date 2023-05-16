#!/usr/bin/env python3

import os, time, datetime, shutil
from os import chdir, getcwd, listdir
from os.path import isfile
cam = ('/home/prints/docker-volumes/the-matrix-api/uploads/prints')
chdir(cam)
messelecionado = 12
print(getcwd())
for c in listdir():
    if isfile(c):
        created = os.path.getmtime(c)
        year,month,day,hour,minute,second=time.localtime(created)[:-3]

        if(month == messelecionado):
            print(c, "--> Mês:%02d"%(month))
            source = f'/home/prints/docker-volumes/the-matrix-api/uploads/prints/{c}'
            destination = f'/home/prints/docker-volumes/the-matrix-api/uploads/prints/printsDezembro2021'
            shutil.move(source,destination)
