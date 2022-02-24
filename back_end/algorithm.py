import numpy as np
from numpy.core.fromnumeric import trace
import scipy.io as scio
from sklearn.model_selection import GridSearchCV
from sklearn import neighbors
import matplotlib.pyplot as plt
import statsmodels.api as sm
import torch


# 定位精度，定义为Euclidean距离
def accuracy(predictions, labels):
    return np.sqrt(np.sum((predictions - labels) ** 2, 1))


def KNN(train_rss, test_rss, train_location):
    # 交叉验证，在knn中用来选择最优的参数K
    test = []
    test.append(test_rss)
    parameters = {'n_neighbors': range(1, 50)}  # 创建等待验证的参数列表
    knn_reg = neighbors.KNeighborsRegressor(
        weights='uniform', metric='euclidean')  # 创建knn算法对象
    clf = GridSearchCV(knn_reg, parameters)  # 在给定列表中调整k值，找到knn模型的最佳k值
    clf.fit(train_rss, train_location)  # 对模型进行拟合
    scores = clf.cv_results_['mean_test_score']  # 输出所有k值的得分
    k = np.argmax(scores)  # 选择score最大的k
    print(k)

    # 使用最优的k做knn回归
    knn_reg = neighbors.KNeighborsRegressor(
        n_neighbors=k, weights='uniform', metric='euclidean')  # 利用最优的k值构建knn模型
    predictions = knn_reg.fit(train_rss, train_location).predict(
        test)  # 利用knn模型对offline_data进行拟合，并对online_data进行预测
    # acc = accuracy(predictions, trace) #利用预测值和真实值计算准确度
    # print("accuracy : ",acc/100, "m")
    print(predictions[0])
    return predictions[0]

# 计算ndarray的均值矩阵


def mean_array(data):
    print(data.shape)
    data_row = data.shape[1]
    data_r = np.mean(data, axis=1).reshape(-1, 1)
    temp = data_r
    for i in range(data_row-1):
        data_r = np.hstack((data_r, temp))
    return data_r

# wk_nnc算法


def wk_nnc(distances):
    return ((distances[:, -1][:, np.newaxis] - distances) + 1e-6) / (
        (distances[:, -1] - distances[:, 0])[:, np.newaxis] + 1e-6)  # 1e-6为了防止除0发生


def best_k_value(its_weights, its_p, offline_rss, offline_location):
    parameters = {'n_neighbors': range(1, 50)}  # 创建等待验证的参数列表
    reg = neighbors.KNeighborsRegressor(
        weights=its_weights, p=its_p)  # 创建knn算法对象
    clf = GridSearchCV(reg, parameters)  # 在给定列表中调整k值，找到knn模型的最佳k值
    clf.fit(offline_rss, offline_location)  # 对模型进行拟合
    scores = clf.cv_results_['mean_test_score']  # 输出所有k值的得分
    best_k = np.argmax(scores)  # 选择score最大的k
    return best_k


def calc_acc(its_neighbors, its_weights, its_p, offline_rss, offline_location, rss, trace):
    reg = neighbors.KNeighborsRegressor(
        n_neighbors=its_neighbors, weights=its_weights, p=its_p)  # 利用最优的k值构建knn模型
    predictions = reg.fit(offline_rss, offline_location).predict(
        rss)  # 利用knn模型对offline_data进行拟合，并对online_data进行预测
    acc = accuracy(predictions, trace)  # 利用预测值和真实值计算准确度
    # print("accuracy : ", acc, "m")
    return acc

# 用于对比NN、KNN、WKNN三种算法的CDF
# 此处返回的参数用于绘图


def compare(train_rss, test_rss, train_location, test_location):
    # 数据导入
    offline_rss = np.array(train_rss)
    offline_location = np.array(train_location)
    rss = np.array(test_rss)
    trace = np.array(test_location)
    # 求每列均值
    mean_offline_location = mean_array(offline_location)
    mean_offline_rss = mean_array(offline_rss)
    mean_trace = mean_array(trace)
    mean_rss = mean_array(rss)

    # 求每位的均值
    offline_location = offline_location/mean_offline_location
    offline_rss = offline_rss/mean_offline_rss
    trace = trace/mean_trace
    rss = rss/mean_rss

    best_k_knn = best_k_value(
        "uniform", 2, offline_rss, offline_location)  # 计算KNN最好的K值
    best_k_wk_nnc = best_k_value(
        wk_nnc, 2, offline_rss, offline_location)  # 计算WKNN最好的K值
    accNN = calc_acc(1, "uniform", 2, offline_rss,
                     offline_location, rss, trace)
    accKNN = calc_acc(best_k_knn, "uniform", 2, offline_rss,
                      offline_location, rss, trace)
    accWK_NNC = calc_acc(best_k_wk_nnc, wk_nnc, 2,
                         offline_rss, offline_location, rss, trace)
    cdf_NN = sm.distributions.ECDF(accNN)
    cdf_KNN = sm.distributions.ECDF(accKNN)
    cdf_WK_NNC = sm.distributions.ECDF(accWK_NNC)
    return accNN, accKNN, best_k_knn, accWK_NNC, best_k_wk_nnc, cdf_NN, cdf_KNN, cdf_WK_NNC
