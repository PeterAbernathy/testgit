import matplotlib.pyplot as plt

squares = [1,4,9,16,25,324,2,3,55,2,325,6,56,54,3,42,4,32,4,423,5,65,2,1,65,8,90,5
    ,1,23,2323,5,23,643,6,1,4,9,16,25,324,2,3,55,2,325,6,56,54,3,42,4,32,4,423,5,
           65,2,1,65,8,90,5,1,23,2323,5,23,643,6,]



plt.plot(squares, linewidth=2)
plt.title('demo',fontsize=14)
plt.xlabel('value',fontsize=14)
plt.ylabel('square of lines', fontsize = 14)
plt.show()
