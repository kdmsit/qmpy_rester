from qmpy_rester import *
import pandas as pd
import argparse
import os.path
from pathlib import Path
import pickle as pkl




def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-index', type=int,default=0,  help='Start Index')
    parser.add_argument('--end-index', type=int,default=600000,  help='End Index')
    args = parser.parse_args()
    return args

args = args_parse()
start_index=args.start_index
end_index=args.end_index
print(start_index)
print(end_index)
out = open("out_id.txt", "w")
data=pd.read_csv("oqmd_new.csv").values[:,0]
property=pd.read_csv("oqmd_new.csv").values[:,5]
fetched_data=[]
id_property=[]
for i in range(start_index,end_index):

    my_file = Path('data_poscar/'+str(i+1) + ".vasp")
    if my_file.is_file():
        continue
    print(i)
    out.writelines(str(i))


out.close()
