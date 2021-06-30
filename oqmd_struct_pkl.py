from qmpy_rester import *
import pandas as pd
import argparse
import pickle as pkl


def write_poscar(structure,index):
    out = open('data_poscar/'+str(index) + ".vasp", "w")
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


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-index', type=int,default=0,  help='Start Index')
    parser.add_argument('--end-index', type=int,default=10,  help='End Index')
    args = parser.parse_args()
    return args

args = args_parse()
start_index=args.start_index
end_index=args.end_index
print(start_index)
print(end_index)
out = open("out.txt", "w")
data=pd.read_csv("oqmd_new.csv").values[:,0]
property=pd.read_csv("oqmd_new.csv").values[:,5]
fetched_data=[]
id_property=[]
for i in range(start_index,end_index):
#for i in range(50):
    composition=data[i]
    delta = property[i]
    print(i, composition)
    with rester.QMPYRester() as q:
        args = {
            # "composition": 'ClW,SrSe'
            "composition": composition
            }
        list_of_data = q.get_oqmd_phases(**args)
    if(list_of_data['data'] !=None):
        if (len(list_of_data['data'])>0):
            structure=list_of_data['data'][0]
            # bgap=structure['band_gap']
            # delta_dft=structure['delta_e']
            # write_poscar(structure,i+1)
            pkl_out = open("data_pickel/obj_"+str(i+1), "wb")
            pkl.dump(structure, pkl_out)
            pkl_out.close()

out.close()
