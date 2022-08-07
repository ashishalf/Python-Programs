from matplotlib import colors
import matplotlib.pyplot as plt
plt.bar([1, 2, 3, 4],[2,3,4,6])
plt.bar([3,5,7,5],[3,7,4,5])
plt.xlabel('Some Numbers')
plt.ylabel('Some Numbers')
plt.legend()
plt.show()