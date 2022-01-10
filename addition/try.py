# 用户：夜卜小魔王
# 时间：2022/1/10 9:38

import numpy as np


a = np.array([[1, 4], [2, 2]])
b = np.mean(a, axis=1).reshape(2, 1)
print(a.shape)
print(np.hstack((b, b)))
print(a/np.hstack((b, b)))