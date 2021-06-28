import fnmatch
import os,sys
from ase import *
from ase.io import *
# from ase.utils import *
import numpy as np
import ase.io.vasp

#### Kishalay, please install ase (atomistic simulation environment)
### I hope it is already installed in
## your machine as you are using pymatgen
## other wise make a pip install
## Run this script in the directory
## where all the .POSCAR files are there

path='data_poscar/'
list=[]
for file in os.listdir('%s'%(path)):
    if fnmatch.fnmatch(file, '*.vasp'):
       list.append(file)

print(np.size(list))

for z in list:
    name=int(z.split('.')[0])
    bulk=read('data_poscar/'+str(z),format='vasp')
    filename='data_cif/'+str(name)+'.cif'
    ase.io.write(filename,bulk)