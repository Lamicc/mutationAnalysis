#python 2.7

from Bio.PDB import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

parser = MMCIFParser()
#pdbl = PDBList()
#pdbl.retrieve_pdb_file('5GL1')

##load a mmcif file
struct = parser.get_structure('5gl1', '5gl1.cif')
#mmcif_dict = MMCIF2Dict('5t15.cif')

##get meta data(if any)
#print struct.header.keys()
#print struct.header["name"]
#print struct.header["release_date"]
#print struct.header["resolution"]

##get models
it = struct.get_models()
models = list(it)
print models

##get chains
chains = list(models[0].get_chains())
print chains

x = []
y = []
z = []

for i in [2434,4838,615,2206,4808,4630,4939]:#240,965
    #for chain in chains:
    #    if len(chain)>200:
            chain = chains[0]
            #print chain
            #residues = list(chain.get_residues())
            residue = chain[i]
            #print len(residues)
            print residue
            atom = residue['CA']
            x.append(atom.get_coord()[0])
            y.append(atom.get_coord()[1])
            z.append(atom.get_coord()[2])
            #print is_aa(residue)
            #atoms = list(residue.get_atoms())
            #print atoms

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=['b','b','b','b','r','r','r'])
plt.show()
#residues = list(chains[0].get_residues())
#print residues


##get atoms
#atoms = list(residues[0].get_atoms())
#print atoms

##get 3D coordinate
#print atoms[0].get_vector()

"""for res in models[0].get_residues():
    print res
"""
