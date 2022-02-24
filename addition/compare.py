# 用户：夜卜小魔王
# 时间：2022/1/9 20:03

import numpy as np
import scipy.io as scio
import statsmodels.api as sm
from sklearn import neighbors
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV


# 计算ndarray的均值矩阵
def mean_array(data):
    data_row = data.shape[1]
    data_r = np.mean(data, axis=1).reshape(-1, 1)
    temp = data_r
    for i in range(data_row-1):
        data_r = np.hstack((data_r, temp))
    return data_r


# 导入离线文件和在线文件
offline_data = scio.loadmat(r'..\database\offline_data.mat')
online_data = scio.loadmat(r'..\database\online_data.mat')
# 分别获取离线文件和在线文件的rss指纹以及位置
offline_location, offline_rss = offline_data['offline_location'], offline_data['offline_rss']  # 训练集
trace, rss = online_data['trace'], online_data['rss']  # 测试集
# 删除无关变量，释放内存空间
del online_data
del offline_data

# mean_offline_location = mean_array(offline_location)
# mean_offline_rss = mean_array(offline_rss)
# mean_trace = mean_array(trace)
# mean_rss = mean_array(rss)
#
# offline_location = offline_location/mean_offline_location
# offline_rss = offline_rss/mean_offline_rss
# trace = trace/mean_trace
# rss = rss/mean_rss

# print(np.mean(offline_location, axis=1).shape)
# print(np.mean(offline_rss, axis=1).shape)
# print(np.mean(rss, axis=1).shape)
# print(np.mean(trace, axis=1).shape)


# 定位精度，定义为Euclidean距离
def accuracy(predict_labels, labels):
    return np.sqrt(np.sum((predict_labels - labels) ** 2, 1))


# wk_nnc算法
def wk_nnc(distances):
    return ((distances[:, -1][:, np.newaxis] - distances) + 1e-6) / (
            (distances[:, -1] - distances[:, 0])[:, np.newaxis] + 1e-6)  # 1e-6为了防止除0发生


def best_k_value(its_weights, its_p):
    parameters = {'n_neighbors': range(1, 50)}  # 创建等待验证的参数列表
    reg = neighbors.KNeighborsRegressor(weights=its_weights, p=its_p)  # 创建knn算法对象
    clf = GridSearchCV(reg, parameters)  # 在给定列表中调整k值，找到knn模型的最佳k值
    clf.fit(offline_rss, offline_location)  # 对模型进行拟合
    scores = clf.cv_results_['mean_test_score']  # 输出所有k值的得分
    best_k = np.argmax(scores)  # 选择score最大的k
    return best_k


def calc_acc(its_neighbors, its_weights, its_p):
    reg = neighbors.KNeighborsRegressor(n_neighbors=its_neighbors, weights=its_weights, p=its_p)  # 利用最优的k值构建knn模型
    predictions = reg.fit(offline_rss, offline_location).predict(rss)  # 利用knn模型对offline_data进行拟合，并对online_data进行预测
    acc = accuracy(predictions, trace)  # 利用预测值和真实值计算准确度
    # print("accuracy : ", acc, "m")
    return acc


def compare_cdf():
    best_k_knn = best_k_value("uniform", 2)
    best_k_wk_nnc = best_k_value(wk_nnc, 2)
    accNN = calc_acc(1, "uniform", 2)
    accKNN = calc_acc(best_k_knn, "uniform", 2)
    accWK_NNC = calc_acc(best_k_wk_nnc, wk_nnc, 2)
    cdf_NN = sm.distributions.ECDF(accNN)
    cdf_KNN = sm.distributions.ECDF(accKNN)
    cdf_WK_NNC = sm.distributions.ECDF(accWK_NNC)
    plt.step(np.linspace(min(accNN), max(accNN)), cdf_NN(np.linspace(min(accNN), max(accNN))), label="NN")
    plt.step(np.linspace(min(accKNN), max(accKNN)), cdf_KNN(np.linspace(min(accKNN), max(accKNN))),
             label=f"KNN(k={best_k_knn})")
    plt.step(np.linspace(min(accWK_NNC), max(accWK_NNC)), cdf_WK_NNC(np.linspace(min(accWK_NNC), max(accWK_NNC))),
             label=f"WK_KNN(k={best_k_wk_nnc})")
    plt.xlabel('distance estimation error(m)'), plt.ylabel('percentage')
    plt.legend()
    # plt.savefig('NN_KNN_WKNNC.jpg')
    plt.show()


if __name__ == '__main__':
    compare_cdf()
