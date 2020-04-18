import pylab
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates
x=[]
y=[]
time=[]
data = open('input.txt', 'r')
i=0
sum_bytes=0
stroka=''
mc=0
for row in data.readlines():
    str=row.split(' ')
    counter=0
    while counter< len(str):
        if str[counter] =="":
            del str[counter]
        else:
            counter +=1
        ip_src=str[4].split(':')
    if ip_src[0]=="192.168.250.3":
        time=str[1].split(':')
        last=time[2].split('.')
        del time[2]
        time.append(last[0])
        time.append(last[1])
        h=int(time[0])
        m=int(time[1])
        s=int(time[2])
        ml=int(time[3])
        mc=h*60*60000+m*60000+s*1000+ml
        x.append(mc)
        y.append(float(str[8]))
        sum_bytes += float(str[8])
        x.sort()
bill = round(((sum_bytes/1024-1000)*0.5),2)
print('Bill for interner: ', bill)
plt.xlabel('Time in mc')
plt.ylabel('Bytes')
plt.plot(x,y)
pylab.show()

