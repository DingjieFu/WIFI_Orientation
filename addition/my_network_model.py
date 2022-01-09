# 用户：夜卜小魔王

import torch.nn as nn


class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.features = nn.Sequential(
            nn.Linear(30, 20),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.2),
            nn.Linear(20, 10),
            nn.ReLU(inplace=True),
            nn.Linear(10, 2)
        )

    def forward(self, x):
        x = self.features(x)
        return x


if __name__ == '__main__':
    model = MyNet()
    print(model)
