import matplotlib.pyplot as plt

inputb=list(range(1,1001,100))
squares=[x**2 for x in inputb]
# plt.plot(inputb,squares,linewidth=5,color='r')



plt.title("sqare nums",fontsize=24)
plt.xlabel("Value",fontsize=13)
plt.ylabel("squares",fontsize=14)

plt.tick_params(axis='both',labelsize='small',right=True)
plt.scatter(inputb,squares,s=20,c=squares,cmap='Blues',edgecolor=None)

plt.show()
# plt.savefig("xx.png",bbox_inches='tight')
