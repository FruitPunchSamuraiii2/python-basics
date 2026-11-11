from numpy import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

x = np.random.randint(2, size = (10))
print(x)

array = np.random.randint(10, 51, size = (3, 3))
print(array)

samples = np.random.normal(loc = 0.0, scale = 1.0, size = 100)
print("The first 10 samples are: ")
print(samples[:10])

uniform_samples = np.random.uniform(low = -5.0, high = 5.0, size = 50)
print(uniform_samples)

normal_samples = random.normal(loc = 0, scale = 1.0, size = 500)
print(normal_samples[:10])
plt.hist(normal_samples)
plt.show()

panda_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
}

panda_var = pd.DataFrame(panda_data)
print(panda_var)

