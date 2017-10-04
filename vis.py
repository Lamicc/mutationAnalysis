from mmtf import fetch

# Get the data for 4CUP
decoded_data = fetch("4CUP")

# Print the number of chains
print("PDB Code: " +str(decoded_data.structure_id)+" has "+str(decoded_data.num_chains)+" chains")

print("Group name:"+str(decoded_data.group_list[0]["groupName"])+"has the following atomic charges: "+",".join([str(x) for x in decoded_data.group_list[0]["formalChargeList"]]))

print("PDB Code:"+str(decoded_data.structure_id)+" has "+str(len(decoded_data.bio_assembly))+" bioassemblies")
