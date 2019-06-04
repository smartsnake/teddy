import numpy as np
import teddy as td
import pandas as pd
import time

# Make a Pandas DataFrame with mixed types
p = pd.DataFrame({
	'c0': pd.Categorical(list('ababababab'), categories=['a', 'b'], ordered=True),
	'c1': [0.0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9],
	'c2': pd.Categorical(list('ababababab'), categories=['a', 'b'], ordered=True),
	'c3': [0.0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9],
	'c4': pd.Categorical(list('ababababab'), categories=['a', 'b'], ordered=True),
	'c5': [0.0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9],
	'c6': pd.Categorical(list('ababababab'), categories=['a', 'b'], ordered=True),
	'c7': [0.0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9],
	'c8': pd.Categorical(list('ababababab'), categories=['a', 'b'], ordered=True),
	'c9': [0.0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9],
	})

# Measure the cost of slicing it
a = time.time()
for i in range(10000):
    q = p.iloc[i % 10]
b = time.time()


# Make a Teddy Tensor with mixed types
t = td.Tensor(np.array([
    [0, 0.0, 0, 0.0, 0, 0.0, 0, 0.0, 0, 0.0],
    [1, 1.1, 1, 1.1, 1, 1.1, 1, 1.1, 1, 1.1],
    [0, 2.2, 0, 2.2, 0, 2.2, 0, 2.2, 0, 2.2],
    [1, 3.3, 1, 3.3, 1, 3.3, 1, 3.3, 1, 3.3],
    [0, 4.4, 0, 4.4, 0, 4.4, 0, 4.4, 0, 4.4],
    [1, 5.5, 1, 5.5, 1, 5.5, 1, 5.5, 1, 5.5],
    [0, 6.6, 0, 6.6, 0, 6.6, 0, 6.6, 0, 6.6],
    [1, 7.7, 1, 7.7, 1, 7.7, 1, 7.7, 1, 7.7],
    [0, 8.8, 0, 8.8, 0, 8.8, 0, 8.8, 0, 8.8],
    [1, 9.9, 1, 9.9, 1, 9.9, 1, 9.9, 1, 9.9],
    ]),
    td.MetaData([
        {0:'a', 1:'b'}, None, {0:'a', 1:'b'}, None, {0:'a', 1:'b'},
        None, {0:'a', 1:'b'}, None, {0:'a', 1:'b'}, None],
    1, ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']))

# Measure the cost of slicing it
c = time.time()
for i in range(10000):
    u = t[i % 10]
d = time.time()

# Report results
print("Pandas = " + str(b - a) + " seconds")
print("Teddy = " + str(d - c) + " seconds")

# print(p[1:9])
# print(t[1:9])
