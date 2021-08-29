import fnmatch
import os,sys
from ase import *
from ase.io import *
from pathlib import Path
import numpy as np
import ase.io.vasp

#532067.vasp

# path='../data_poscar/'
path='data_poscar/'
list=[]
for file in os.listdir('%s'%(path)):
    if fnmatch.fnmatch(file, '*.vasp'):
        name = int(file.split('.')[0])
        filename = '../data_cif/' + str(name) + '.cif'
        my_file = Path(filename)
        if my_file.is_file():
            continue
        print(file)
        bulk = read(path + str(file), format='vasp')
        ase.io.write(filename, bulk)


# path='data_poscar/'
# list=[]
# for file in os.listdir('%s'%(path)):
#     if fnmatch.fnmatch(file, '*.vasp'):
#        list.append(file)
#
# print(np.size(list))
#
# for z in list:
#     name=int(z.split('.')[0])
#     bulk=read('data_poscar/'+str(z),format='vasp')
#     filename='data_cif/'+str(name)+'.cif'
#     ase.io.write(filename,bulk)