import matplotlib.pyplot as plt
numbers = [1,546,65465,211,78945,56,5]
plt.title("it's only a joke!",fontsize=24)
plt.xlabel('number',fontsize=15)
plt.ylabel('point',fontsize=15)
plt.tick_params(axis='both',labelsize=14)

plt.plot(numbers)
plt.show()