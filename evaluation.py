import time
import SeqSC
import SC
import Kmeans
from sklearn.metrics.cluster import normalized_mutual_info_score
import matplotlib.pyplot as plt
import numpy as np
ssc = []
nmissc = []
sssc = []
km = []
kmpp = []
nmisc = []
nmikmeans = []
nmikmeansplusplus = []
repeat = 20
till = 15
x_plot = []
print("SeqSC computation")
print(" n  |  time  |  NMI")

for i in range(0,till):
    x_plot.append((i+1)*500)
    nmissc.append(0)
    nmisc.append(0)
    nmikmeansplusplus.append(0)
    nmikmeans.append(0)
    ssc.append(0)
    sssc.append(0)
    km.append(0)
    kmpp.append(0)

for j in range(0,repeat):
    for i in range(0,till):
        n = (i+2) *30
        k = 10
        time_start = time.perf_counter()
        x, y, labels = SeqSC.guiseqsc(k,n,n,1)
        elapsed = time.perf_counter() - time_start
        nmi = normalized_mutual_info_score(y,labels)
        nmissc[i]+=(nmi)
        print(str(n)+" | "+str(elapsed)+"  |  "+str(nmi))
        ssc[i]+= (elapsed)


print("SC computation")
print(" n  |  time  |  NMI")
for j in range(0,repeat):
    for i in range(0,till):
        n = (i+1) *50
        k = 10
        time_start = time.perf_counter()
        x, y, labels = SC.guisc(k,n,1)
        elapsed = time.perf_counter() - time_start
        nmi = normalized_mutual_info_score(y, labels)
        nmisc[i]+=(nmi)
        print(str(n) + " | " + str(elapsed) + "  |  " + str(nmi))
        sssc[i]+=(elapsed)


print("KMeans computation")
print(" n  |  time  |  NMI")
for j in range(0,repeat):
    for i in range(0,till):
        n = (i+1) *50
        k = 10
        time_start = time.perf_counter()
        x, y, labels = Kmeans.guikmeans(k,n,1)
        elapsed = time.perf_counter() - time_start
        nmi = normalized_mutual_info_score(y, labels)
        print(str(n) + " | " + str(elapsed) + "  |  " + str(nmi))
        nmikmeans[i]+=(nmi)
        km[i]+=elapsed


print("KMeans++ computation")
print(" n  |  time  |  NMI")
for j in range(0,repeat):
    for i in range(0,till):
        n = (i+1) *50
        k = 10
        time_start = time.perf_counter()
        x, y, labels = Kmeans.guikmeansplusplus(k,n,1)
        elapsed = time.perf_counter() - time_start
        nmi = normalized_mutual_info_score(y, labels)
        print(str(n) + " | " + str(elapsed) + "  |  " + str(nmi))
        nmikmeansplusplus[i]+=(nmi)
        kmpp[i]+= elapsed

kmpp = np.divide(kmpp,repeat)
km = np.divide(km,repeat)
ssc = np.divide(ssc,repeat)
sssc = np.divide(sssc,repeat)
nmisc = np.divide(nmisc,repeat)
nmikmeansplusplus = np.divide(nmikmeansplusplus,repeat)
nmikmeans = np.divide(nmikmeans,repeat)
nmissc = np.divide(nmissc,repeat)
sssc = np.array(sssc)
nmisc = np.array(nmisc)
nmikmeansplusplus = np.array(nmikmeansplusplus)
nmissc = np.array(nmissc)
nmikmeans = np.array(nmikmeans)
ssc = np.array(ssc)
print(nmissc)
print(sssc)

fig, xy_time = plt.subplots()
fig, xy_nmi = plt.subplots(tight_layout=True)
xy_time.plot(x_plot, km, '-d',c= "blue", label = 'KMeans')
xy_time.plot(x_plot, kmpp, '-^',c= "yellow", label = 'KMeans++')
xy_time.plot(x_plot, ssc, '-d',c= "red", label = 'SC')
xy_time.plot(x_plot, sssc,'--o',c= "green",linewidth=2, label='SeqSC')
xy_time.legend(loc='upper left')
xy_time.set_xlabel('x Word')
xy_time.set_ylabel('time (s)')
xy_time.set_title("Time SC - SSC")

xy_nmi.plot(x_plot, nmikmeans, '-d',c= "blue", label = 'KMeans')
xy_nmi.plot(x_plot, nmikmeansplusplus, '-^',c= "yellow", label = 'KMeans++')
xy_nmi.plot(x_plot, nmisc, '-X',c= "red", label = 'SC')
xy_nmi.plot(x_plot, nmissc,'--o',c= "green",linewidth=2, label='SeqSC')
xy_nmi.legend(loc='upper left')
xy_nmi.set_xlabel('x Word')
xy_nmi.set_ylabel('NMI')
xy_nmi.set_title("NMI")



print("NMI computation : ")
print(x)
print("SeqSC : "+str(nmissc))
print("SC : "+str(nmisc))
print("KMeans : "+str(nmikmeans))
print("KMeans++ : "+str(nmikmeansplusplus))


plt.show()