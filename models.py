import torch
import torch.nn as nn


"""
class MyNN(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def forward(self, *args):
        pass
"""

"""
nn.Sequential()
nn.ModuleList()
nn.ModuleDict()
"""
# 1.
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)

# 2.
model = nn.Sequential()
model.add_module('layer_1', nn.Linear(784, 128))
model.add_module('ReLu', nn.ReLU())
model.add_module('layer_2', nn.Linear(128, 10))

class MyNN(nn.Module):
    def __init__(self, input, output):
        super().__init__()
        self.layer_1 = nn.Linear(input, 128)
        self.act = nn.ReLU()
        self.layer_2 = nn.Linear(128, output)

    def forward(self, x):
        x = self.layer_1(x)
        x = self.act(x)
        out = self.layer_2(x)
        return out


class MyNN1(nn.Module):
    def __init__(self, input, output):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input, 128),
            nn.ReLU(),
            nn.Linear(128, output)
        )

    def forward(self, x):
        out = self.model(x)
        return out


class MyNN2(nn.Module):
    def __init__(self, input, output):
        super().__init__()
        self.layer_1 = nn.Linear(input, 128)
        self.act = nn.ReLU()
        self.layer_2 = nn.Linear(128, output)

    def forward(self, x, y):
        x = self.layer_1(x)
        x = self.act(x + y)
        out = self.layer_2(x)
        return out


class MyNN3(nn.Module):
    def __init__(self, input, output):
        super().__init__()
        self.layer_1 = nn.Linear(input, 128)
        self.act = nn.ReLU()
        self.layer_2 = nn.Linear(128, output)

    def forward(self, x, y):
        x = self.layer_1(x)
        x = self.act(x + y)
        out = self.layer_2(x)
        return out, x


class MyNN4(nn.Module):
    def __init__(self, input, output, hidden_size = 2048):
        super().__init__()
        layers = []
        for i in range(10):
            layers.append(nn.Linear(input, hidden_size))
            layers.append(nn.ReLU())
            input = hidden_size
            hidden_size //= 2
        layers.append(nn.Linear(input, output))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        out = self.model(x)
        return out


# def prob(x, y, z, v):
#     print(x + y + z + v)
#
#
# l = [22, 33, 44, 55]
# print(l)
# print(*l)
# prob(*l)