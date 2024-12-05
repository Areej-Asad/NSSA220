# review ex1
# generate 1000 random integers between 1-9. 
# code to draw horizontal bar plot shows the frequency (i.e., count) 
# of each number between 1-9 in list. show proper labels for x-axis & y-axis. 

import matplotlib.pyplot as plt
import numpy as np
from random import randrange
lst = [ randrange(1,10) for i in range(1000)]

import matplotlib.pyplot as plt
from collections import Counter

from random import randrange
lst = [randrange(1, 10) for _ in range(1000)]

frequency = Counter(lst)

numbers = list(frequency.keys())
counts = list(frequency.values())

plt.barh(numbers, counts, color='blue')

plt.xlabel('Frequency')
plt.ylabel('Number')
plt.title('Frequency of Numbers (1 to 9) in Random List')

plt.show()
