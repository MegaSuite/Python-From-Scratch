import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.


while True:
    rw=RandomWalk(5000)
    rw.fill_walk()
    plt.figure(figsize=(10,6))
    # plt.scatter(rw.x_values,rw.y_values,s=100,c=rw.y_values,cmap='Blues',edgecolor=None)
    # plt.scatter(0,0,c='green',edgecolor='none',s=200)
    # plt.scatter(rw.x_values[-1],rw.y_values[-1],c='blue',edgecolor='none',s=200)


    plt.plot(rw.x_values,rw.y_values,linewidth=1)

    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.axis('off')



    plt.show()
    keep_running=input("Make another walk? (y/n): ")
    if keep_running=='n':
        break