import matplotlib.pyplot as plt

value=[]

for i in range(0,1080):
    value.append(i)

point=[]

for i in value:
    a = i**2
    point.append(a)

plt.scatter(value,point,c=value, cmap=plt.cm.Blues,edgecolor='none',s=1)

plt.title('it is a joke',fontsize=15)
plt.xlabel('value',fontsize=15)
plt.ylabel('point',fontsize=15)
plt.tick_params(axis='both',which='both',labelsize=14)

plt.show()