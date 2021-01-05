

from qmpy_rester import *
# import qmpy as qmpy
import  pickle as pkl
import json
from pymatgen.core.structure import Structure
import pandas as pd

def write_poscar(structure,index):
    name_list=[]
    count_list=[]
    out = open('exp_data_bgap/'+str(index) + ".vasp", "w")
    site_count={}
    sites_list=[]
    sites = structure["sites"]
    for s in sites:
        s=s.split('@')
        s_name=s[0].strip()
        if s_name in site_count:
            site_count[s_name] = site_count[s_name]+1
        else:
            site_count[s_name]=1
        site=[]
        for c in s[1].strip().split(' '):
            site.append(c)
        sites_list.append(site)
        
    for n in site_count.keys():
        out.write(n)
        out.write(' ')
    out.writelines("\n")
    out.writelines('1.00')
    out.writelines("\n")

    # composition=structure["composition"]
    # for n in composition.split(' '):
    #     name=n[0:len(n)-1]
    #     count=n[-1]
    #     name_list.append(name)
    #     count_list.append(count)
    #     out.write(name)
    #     out.write(' ')
    # out.writelines("\n")
    # out.writelines('1.00')
    # out.writelines("\n")

    unit_cell=structure["unit_cell"]
    for cell in unit_cell:
        for i in cell:
            out.write(str(i))
            out.write(' ')
        out.writelines("\n")

    for n in site_count.keys():
        out.write(n)
        out.write(' ')
    out.writelines("\n")

    for name,count in site_count.items():
        out.write(str(count))
        out.write(' ')
    out.writelines("\n")
    out.writelines('Direct')
    out.writelines("\n")

    for site in sites_list:
        for s in site:
            out.write(s)
            out.write(' ')
        out.writelines("\n")
    out.close()




data=pd.read_csv("exp_data/experimental_prop.csv").values[:,0]
property=pd.read_csv("exp_data/experimental_prop.csv").values[:,1]
id_property=[]
count=1
for i in range(len(data)):
    composition=data[i]
    delta = property[i]
    print(i, composition)
    with rester.QMPYRester() as q:
        args = {
            # "composition": 'ClW,SrSe'
            "composition": composition
            }
        list_of_data = q.get_oqmd_phases(**args)
    # if(list_of_data['data'] !=None):
    if (len(list_of_data['data'])>0):
        structure=list_of_data['data'][0]
        bgap=structure['band_gap']
        write_poscar(structure,count)
        id_property.append([count,delta])
        count=count+1
my_df = pd.DataFrame(id_property)
my_df.to_csv('exp_data_bgap/id_prop.csv', index=False, header=False)
