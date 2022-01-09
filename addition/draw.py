# 用户：夜卜小魔王
# 时间：2022/1/8 15:41

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_datasets():
    dataset_path = "DJ_fingerprint/test_dj.csv"
    dataset_loader = pd.read_csv(dataset_path, index_col=0)
    row = dataset_loader.shape[0]  # 数据的行数 234行 索引为 0~233
    datasets = np.array([0, 0])
    for i in range(row):
        x_label = np.array(dataset_loader.iloc[i, :])[30:31]
        y_label = np.array(dataset_loader.iloc[i, :])[31:32]
        datasets = np.vstack((datasets, np.append(x_label, y_label)))
    return datasets[1:]


def draw_heatmap():
    sns.set()
    ax = sns.heatmap(get_datasets())
    plt.show()


def draw_():
    dataset_loader = pd.read_csv("DJ_fingerprint/train_dj.csv", index_col=0)
    sns.set()
    with sns.axes_style("white"):
        sns.jointplot(x="xLabel", y="yLabel", data=dataset_loader)
        sns.jointplot(x="xLabel", y="yLabel", data=dataset_loader, kind="hex")
        sns.jointplot(x="xLabel", y="yLabel", data=dataset_loader, kind="hist")
        sns.jointplot(x="xLabel", y="yLabel", data=dataset_loader, kind="kde")
        sns.jointplot(x="xLabel", y="yLabel", data=dataset_loader, kind="reg")
        sns.jointplot(
            x="xLabel", y="yLabel", data=dataset_loader,
            marker="+", s=100, marginal_kws=dict(bins=25, fill=False)
        )
    plt.show()


if __name__ == '__main__':
    # draw_heatmap()
    draw_()
    pass
