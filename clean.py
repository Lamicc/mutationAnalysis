#python 3
import pandas as pd
from random import shuffle

#import data
df = pd.read_csv("./csv/clinvar_result.csv")
df = df[df['Name'].str.contains('\(p.*')]
for i in df.index:
    aa = filter(str.isdigit, df.Name.str.split()[i][1])
    if len(aa)>4:
        df.loc[i,'Amino_acid'] = aa[:len(aa)/2]
    else:
        df.loc[i,'Amino_acid'] = aa

#congenital myopathy group
df_my = df[df['Condition(s)'].str.contains('disease|myopathy',case=False)]
df_my.loc[:,'Label'] = 1
#li = df_my.Amino_acid.tolist()
#shuffle(li)
#print('+'.join(li))

#malignant hyperthermia group
temp = df[~df['Condition(s)'].str.contains('disease|myopathy',case=False)]
df_hy = temp[temp['Condition(s)'].str.contains('hyperthermia',case=False)]
df_hy.loc[:,'Label'] = 0
#li = df_hy.Amino_acid.tolist()
#shuffle(li)
#print('+'.join(li))

newdf = pd.concat([df_my,df_hy])
supdf = df.drop(newdf.index)
supdf.loc[:,'Label'] = -1
newdf = pd.concat([newdf,supdf])
newdf = newdf.reset_index(drop=True)
newdf.to_csv("./csv/dataframe.csv",index=False)

#df_my.to_csv("./my.csv")
#df_hy.to_csv("./hy.csv")
