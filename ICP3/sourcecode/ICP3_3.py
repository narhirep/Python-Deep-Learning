import numpy as np

#creating a random vector of size 20
num = np.random.randint(1, high=20, size=20, dtype='int');
print('Random array generated',num)

#reshaping the array to 4 by 5
num = np.reshape(num, (4,5));
print('Reshape the array to 4 by 5',num)

#replacing the max in each row by 0
print('Replacing Max No. by 0',np.where(num == np.max(num, axis=1).reshape(-1,1), 0, num))