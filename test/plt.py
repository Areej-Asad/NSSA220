# review ex1
# generate 1000 random integers between 1-9. 
# code to draw horizontal bar plot shows the frequency (i.e., count) 
# of each number between 1-9 in list. show proper labels for x-axis & y-axis. 

import matplotlib.pyplot as plt
import numpy as np
from random import randrange

# Generate random numbers
lst = [randrange(1, 10) for i in range(1000)]

# Count frequencies of numbers from 1 to 9
frequencies = [lst.count(i) for i in range(1, 10)]

# Plot the horizontal bar chart
plt.barh(range(1, 10), frequencies, color='blue')
plt.xlabel("Frequency")
plt.ylabel("Number")
plt.title("Frequency of Numbers from 1 to 9")
plt.show()

