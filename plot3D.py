#python 2.7/3

from Bio.PDB import *
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

parser = MMCIFParser()
#pdbl = PDBList()
#pdbl.retrieve_pdb_file('5GL1')

##load a mmcif file
struct = parser.get_structure('5gl1', './mmcif/5gl1.cif')

##get meta data(if any)
#print struct.header.keys()
#print struct.header["name"]
#print struct.header["release_date"]
#print struct.header["resolution"]

##load dataset
try :
    df = pd.read_csv("./dataframe.csv")
except IOError:
    print("File not found!")

##get models
it = struct.get_models()
models = list(it)

##get chains
chains = list(models[0].get_chains())
#print chains

##create coordinate lists
x = []
y = []
z = []

#for i in [2434,4838,615,2206,4808,4630,4939]:#240,965
for i in df.Amino_acid:
    #for chain in chains:
    #    if len(chain)>200:
            chain = chains[0]
            #print chain
            #residues = list(chain.get_residues())
            try:
                residue = chain[i]
                #print(residue)
                atom = residue['CA']
                x.append(atom.get_coord()[0])
                y.append(atom.get_coord()[1])
                z.append(atom.get_coord()[2])
            except KeyError:
                x.append(None)
                y.append(None)
                z.append(None)

##add columns to store coordinate
x = pd.Series(x,name='x')
y = pd.Series(y,name='y')
z = pd.Series(z,name='z')
df = pd.concat([df,x,y,z], axis=1)

##delete rows without coordinate
df = df.dropna(axis=0, how='any')

df.to_csv("./csv/dataset.csv",index=False)

##delete unlabelled rows
df = df[df.Label>=0]

##set up color list
color = []
for i in df.index:
    if df.loc[i,'Label'] == 1:
        color.append('r')
    else:
        color.append('b')

##plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.x, df.y, df.z,c=color)
plt.show()
