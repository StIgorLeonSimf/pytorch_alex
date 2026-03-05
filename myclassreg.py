import os
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import torch
import torchvision

from torchvision.datasets import ImageFolder
from torch.utils.data import Dataset, DataLoader, random_split


class DatasetReg(Dataset):
    def __init__(self, path, transform=None):
        self.path = path
        self.transform = transform
        self.list_name_file = os.listdir(path)
        if 'coords.json' in self.list_name_file:
            self.list_name_file.remove('coords.json')
        self.len_dataset = len(self.list_name_file)
        with open(os.path.join(self.path, 'coords.json'), 'r') as f:
            self.dict_coords = json.load(f)

    def __len__(self):
        return self.len_dataset

    def __getitem__(self, index):
        name_file = self.list_name_file[index]
        path_img = os.path.join(self.path, name_file)
        # img = np.array(Image.open(path_img))
        img = Image.open(path_img)
        # coord = np.array(self.dict_coords[name_file])
        coord = torch.tensor(self.dict_coords[name_file], dtype=torch.float32)
        if self.transform is not None:
            img = self.transform(img)
        return img, coord


if __name__ == '__main__':
    p = r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\dataset'
    # print(os.listdir(p))
    # print(len(os.listdir(p)))
    dataset = DatasetReg(p)
    print(len(dataset))

    # img, coord = dataset[98800]
    # print(f'Координаты центра: {coord}')
    # plt.scatter(coord[1], coord[0], marker='o', color='red')
    # plt.imshow(img, cmap='gray')
    # plt.show()

    train_set, val_set, test_set = random_split(dataset, [0.7, 0.1, 0.2])
    # print(f'Длина данных для тренировки {len(train_set)}')
    # print(f'Длина данных для валидации {len(val_set)}')
    # print(f'Длина данных для тестирования {len(test_set)}')

    train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
    val_loader = DataLoader(val_set, batch_size=64, shuffle=False)
    test_loader = DataLoader(test_set, batch_size=64, shuffle=False)
    for i, (samples, target) in enumerate(val_loader):
        if i < 3:
            print(f'Номер batch: {i + 1}')
            print(f'  Размер samles: {samples.shape}')
            print(f'  Размер target: {target.shape}')
    print('-----------------')
    print(f'Номер batch: {i + 1}')
    print(f'   Размер samles: {samples.shape}')
    print(f'   Размер target: {target.shape}')
