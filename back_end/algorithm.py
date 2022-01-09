import numpy as np
from numpy.core.fromnumeric import trace
import scipy.io as scio
from sklearn.model_selection import GridSearchCV
from sklearn import neighbors
import matplotlib.pyplot as plt
import torch


# 定位精度，定义为Euclidean距离
def accuracy(predictions, labels):
    return np.mean(np.sqrt(np.sum((predictions - labels) ** 2, 1)))


def KNN(train_rss, test_rss, train_location):
    # 交叉验证，在knn中用来选择最优的参数K
    test = []
    test.append(test_rss)
    parameters = {'n_neighbors': range(1, 50)}  # 创建等待验证的参数列表
    knn_reg = neighbors.KNeighborsRegressor(weights='uniform', metric='euclidean')  # 创建knn算法对象
    clf = GridSearchCV(knn_reg, parameters)  # 在给定列表中调整k值，找到knn模型的最佳k值
    clf.fit(train_rss, train_location)  # 对模型进行拟合
    scores = clf.cv_results_['mean_test_score']  # 输出所有k值的得分
    k = np.argmax(scores)  # 选择score最大的k
    print(k)

    # 使用最优的k做knn回归
    knn_reg = neighbors.KNeighborsRegressor(n_neighbors=k, weights='uniform', metric='euclidean')  # 利用最优的k值构建knn模型
    predictions = knn_reg.fit(train_rss, train_location).predict(test)  # 利用knn模型对offline_data进行拟合，并对online_data进行预测
    # acc = accuracy(predictions, trace) #利用预测值和真实值计算准确度
    # print("accuracy : ",acc/100, "m")
    print(predictions[0])
    return predictions[0]
