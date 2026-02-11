import torch
import torchvision

from torchvision.datasets import ImageFolder
from torch.utils.data import Dataset, DataLoader, random_split

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class MnistDataset(Dataset):
    def __init__(self, path, transform=None):
        self.path = path
        self.transform = transform
        self.len_dataset = 0
        self.data_list = []
        for path_dir, dir_list, file_list in os.walk(path):
            if path_dir == path:
                self.classes = dir_list
                self.class_to_idx = {
                    cls_name: i for i, cls_name in enumerate(self.classes)
                }
                continue
            cls = path_dir.split("\\")[-1]
            for name_file in file_list:
                file_path = os.path.join(path_dir, name_file)
                self.data_list.append((file_path, self.class_to_idx[cls]))
            self.len_dataset += len(file_list)

    def __len__(self):
        return self.len_dataset

    def __getitem__(self, index):
        file_path, target = self.data_list[index]
        sample = np.array(Image.open(file_path))
        if self.transform is not None:
            sample = self.transform(sample)
        return sample, target


if __name__ == '__main__':
    # создание datasets
    train_data = MnistDataset(r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\training')
    test_data = MnistDataset(r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\testing')
    print(train_data.classes)
    print(train_data.class_to_idx)
    for cls, one_hot_position in train_data.class_to_idx.items():
        one_hot_vector = [(i == one_hot_position) * 1 for i in range(10)]
        print(f'\033[32m{cls}\033[0m=>\033[34m{one_hot_vector}\033[0m')
    print(len(train_data))
    print(len(test_data))
    # print(train_data[2564])
    # print(train_data[38564])
    img, one_hot_position = train_data[38564]
    # print(img)
    cls = train_data.classes[one_hot_position]
    print(f'class - {cls}')
    plt.imshow(img, cmap='gray')
    # plt.show()

    # train_data, val_data = random_split(train_data, [0.8, 0.2])
    #
    # train_loader = DataLoader(train_data, batch_size=16, shuffle=True)
    # val_loader = DataLoader(val_data, batch_size=16, shuffle=False)
    # test_loader = DataLoader(test_data, batch_size=16, shuffle=False)
    #
    # for i, (sample, target) in enumerate(test_loader):
    #     if i < 3:
    #         print(f'Номер batch = {i + 1}')
    #         print(f'Размер sample = {sample.shape}')
    #         print(f'Target = {target.shape} ')
    # print('........................')
    # print(f'Номер batch = {i + 1}')
    # print(f'Размер sample = {sample.shape}')
    # print(f'Target = {target.shape} ')

    train_data = ImageFolder(r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\training')
    test_data = ImageFolder(r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\testing')
    print(train_data.classes)
    print(train_data.class_to_idx)
    print(len(train_data))
    print(len(test_data))
    print(train_data[38564])
    img, one_hot_position = train_data[38564]
    cls =  train_data.classes[one_hot_position]
    print(f'class - {cls}')
    plt.imshow(img, cmap='gray')
    # plt.show()
    train_data, val_data = random_split(train_data, [0.8, 0.2])
    print(len(train_data))
    print(len(val_data))
    print(len(test_data))

    train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
    val_loader = DataLoader(val_data, batch_size=64, shuffle=False)
    test_loader = DataLoader(test_data, batch_size=64, shuffle=False)


