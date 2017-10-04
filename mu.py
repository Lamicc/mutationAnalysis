#python 2.7

from Bio.PDB import *

parser = MMCIFParser()
#pdbl = PDBList()
#pdbl.retrieve_pdb_file('5GL1')

struct = parser.get_structure('5gl1', '5gl1.cif')
#mmcif_dict = MMCIF2Dict('5t15.cif')
#print struct.header.keys()
#print struct.header["name"]
#print struct.header["release_date"]
#print struct.header["resolution"]
struct
