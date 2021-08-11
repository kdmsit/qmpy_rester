import fnmatch
import os,sys
from ase import *
from ase.io import *
# from ase.utils import *
import numpy as np
import ase.io.vasp

path='../data_poscar/'
list=[]
for file in os.listdir('%s'%(path)):
    if fnmatch.fnmatch(file, '*.vasp'):
        name = int(file.split('.')[0])
        bulk = read(path + str(file), format='vasp')
        filename = '../data_cif/' + str(name) + '.cif'
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