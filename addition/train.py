# 用户：夜卜小魔王

import os
import torch
import numpy as np
import pandas as pd
import statsmodels.api as sm
import torch.optim as optim
import matplotlib.pyplot as plt
from my_network_model import MyNet


def get_dataset(path):  # 得到数据集
    dataset_path = path
    dataset_loader = pd.read_csv(dataset_path, index_col=0)
    row = dataset_loader.shape[0]  # 数据的行数 234行 索引为 0~233
    col = dataset_loader.shape[1]  # 数据的列数 34列/实际只有前32列有用 即索引为 0~31
    datasets = list()
    for i in range(row):
        position = list(dataset_loader.iloc[i, :])[:30]
        xy_label = list(dataset_loader.iloc[i, :])[30:32]
        datasets.append((position, xy_label))
    # for data in datasets:
    #     position_, xy_label_ = data
    #     print(f"position:{position_}; xy_label:{xy_label_}")
    return datasets


def my_loss(predict_xy, true_xy):  # 损失函数 定义为距离的均值
    d_tensor = predict_xy - true_xy  # 两个tensor相减 即对应位置的坐标相减
    p_tensor = torch.pow(d_tensor, 2)  # 计算平方值
    sqrt_tensor = torch.sqrt(p_tensor.sum())  #
    return sqrt_tensor


def draw_cdf():
    pretrained_path = "weight/best.pth"
    net = MyNet()
    if os.path.exists(pretrained_path):  # 如果预训练模型存在则加载预训练模型参数
        net.load_state_dict(torch.load(pretrained_path))
        print("Load pretrained weights successfully!")

    loss_function = my_loss
    optimizer = optim.Adam(net.parameters(), lr=0.001)

    train_datasets = get_dataset("DJ_fingerprint/train_dj.csv")  # 训练数据
    val_loader = get_dataset("DJ_fingerprint/test_dj.csv")  # 测试数据
    val_loader = iter(val_loader)

    train_loss_list = list()
    test_loss_list = list()

    for epoch in range(40):
        running_loss = 0.0  # 当前的损失
        running_test_loss = 0.0  # 当前的准确度
        for step, data in enumerate(train_datasets, start=0):
            positions, xy_label = data  # 一组组读入数据
            positions, xy_label = torch.tensor(positions), torch.tensor(xy_label)  # 转成tensor
            # positions为 (30,1) xy_label为(2,1)
            optimizer.zero_grad()  # 梯度清零
            train_outputs = net(positions)  # forward + backward + optimize
            train_loss = loss_function(train_outputs, xy_label)  # 计算损失
            # print(train_loss)
            train_loss.backward()  # 反向传播 backpropagation
            optimizer.step()  # 进行单次优化 更新所有参数

            # print statistics
            running_loss += train_loss.item()
            if step % 200 == 199:  # 每199个mini-batch打印一次
                val_positions, val_label = next(val_loader)

                with torch.no_grad():
                    test_label = net(torch.tensor(val_positions))
                    test_loss = my_loss(test_label, torch.tensor(val_label))

                    save_path = "weight/best.pth"
                    if test_loss >= running_test_loss:  # 保存精度最高的模型
                        torch.save(net.state_dict(), save_path)
                        running_test_loss = test_loss

                    train_loss_list.append(running_loss / 200)
                    test_loss_list.append(test_loss.detach().numpy().tolist())

                    print('[epoch: %d,step: %5d] train_loss: %.3f  test_loss: %.3f' %
                          (epoch + 1, step + 1, running_loss / 200, test_loss.detach().numpy()))
                    running_loss = 0.0

        print('Finished Training!')

        # 训练完才保存参数 因此默认只保存最后一次的训练参数
        save_path = 'weight/last.pth'
        torch.save(net.state_dict(), save_path)  # 只保存模型的参数
        # torch.save(net, save_path)  # 保存整个模型

    # y1 = train_loss_list
    # y2 = test_loss_list
    # x = range(len(y1))
    # plt.plot(x, y1, "r", label="train"), plt.plot(x, y2, "b", label="test")
    # plt.xlabel('mini_batches'), plt.ylabel('loss')
    # plt.legend()
    # plt.show()
    # print(train_loss_list)

    # =============绘制cdf图===============
    cdf_LN = sm.distributions.ECDF(test_loss_list)
    # 等差数列，用于绘制X轴数据
    x = np.linspace(min(test_loss_list), max(test_loss_list))
    # x轴数据上值对应的累计密度概率
    y = cdf_LN(x)
    # 绘制阶梯图
    plt.step(x, y)
    plt.xlabel('distance estimation error(m)'), plt.ylabel('percentage')
    plt.savefig('CDF.jpg')
    plt.show()


if __name__ == '__main__':
    draw_cdf()
