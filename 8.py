from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('8-kmeansdata.csv')
f1 =data['Distance_Feature']
f2=data['Speeding_Feature']
X =np.array(list(zip(f1,f2)))
plt.scatter(f1,f2,color='black')
plt.show()
kmeans = KMeans(3).fit(X)
labels = kmeans.predict(X)
plt.scatter(f1,f2,c=labels)
plt.show()
gm = GaussianMixture(3).fit(X)
labels = gm.predict(X)
plt.scatter(f1,f2,c=labels)
plt.show()
