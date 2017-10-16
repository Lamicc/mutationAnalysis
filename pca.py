#python 2.7

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, KernelPCA

try :
    df = pd.read_csv("./csv/dataset.csv")
except IOError:
    print("File not found!")

df = df[df.Label>=0]
X = df[['x','y','z']]
y = df.Label

#pca = PCA(n_components=2)
#X_new = pca.fit_transform(X)

kpca = KernelPCA(kernel="rbf",fit_inverse_transform=True,gamma = 10)
X_kpca = kpca.fit_transform(X)
X_back = kpca.inverse_transform(X_kpca)

color = []
for i in df.index:
    if df.loc[i,'Label'] == 1:
        color.append('r')
    else:
        color.append('b')

plt.scatter(X_back[:, 0], X_back[:, 1], c=color)

#plt.scatter(X_new[:, 0],X_new[:, 1], c=color)
#plt.xlabel('PCA1')
#plt.ylabel('PCA2')
plt.show()
