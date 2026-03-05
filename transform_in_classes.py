from myclass import MnistDataset
from myclassreg import DatasetReg

import os
import json

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torch
import torchvision

from torchvision.datasets import ImageFolder
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms
from torchvision.transforms import v2


# transform = transforms.Compose(
#     [
#         transforms.ToTensor(),
#         transforms.Normalize(mean=(0.5,), std=(0.5,))
#     ]
# )
#
# train_data = MnistDataset(r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\training', transform)
# test_data = MnistDataset(r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\testing', transform)
#
# img, cls = test_data[2]
# print('img: ')
# print(f'     {type(img)}')
# print(f'     {img.shape}')
# print(f'     {img.dtype}')
# print(f'     min={img.min()}, max={img.max()} ')
# print('cls:  ')
# print(f'     {cls}')
#
# transform = v2.Compose(
#     [
#         v2.ToImage(),
#         # v2.Grayscale(), если делали через ImageFolder и получили 3 цв.канала
#         v2.ToDtype(torch.float32, scale=True),
#         v2.Normalize(mean=(.5,), std=(.5,))
#     ]
# )
#
# train_data, val_data = random_split(train_data, [.8, .2])
# train_loader = DataLoader(dataset=train_data, batch_size=16, shuffle=True)
# val_loader = DataLoader(dataset=val_data, batch_size=16, shuffle=False)
# test_loader = DataLoader(dataset=test_data, batch_size=16, shuffle=False)
#
# imgs, cls = next(iter(train_loader))
# print('imgs: ')
# print(f'     {type(imgs)}')
# print(f'     {imgs.shape}')
# print(f'     {imgs.dtype}')
# print(f'     min={imgs.min()}, max={imgs.max()} ')
# print('cls:  ')
# print(f'     {type(cls)}')
# print(f'     {cls.shape}')
# print(f'     {cls.dtype}')
#
# print()

# transform = v2.Compose(
#     [
#         v2.ToImage(),
#         v2.ToDtype(torch.float32, scale=True),
#         v2.Normalize(mean=(0.5,), std=(0.5,))
#     ]
# )
#
# dataset = DatasetReg(
#     r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\dataset', transform)
# img, coord = dataset[2]
# print('img: ')
# print(f'     {type(img)}')
# print(f'     {img.shape}')
# print(f'     {img.dtype}')
# print(f'     min={img.min()}, max={img.max()} ')
# print('coord:  ')
# print(f'     {type(coord)}')
# print(f'     {coord.shape}')
# print(f'     {coord.dtype}')
#
# train_set, val_set, test_set = random_split(dataset, [0.7, 0.1, 0.2])
# train_loader = DataLoader(dataset=train_set, batch_size=32, shuffle=True)
# val_loader = DataLoader(dataset=val_set, batch_size=32, shuffle=False)
# test_loader = DataLoader(dataset=test_set, batch_size=32, shuffle=False)
#
# imgs, coords = next(iter(train_loader))
# print('imgs: ')
# print(f'     {type(imgs)}')
# print(f'     {imgs.shape}')
# print(f'     {imgs.dtype}')
# print(f'     min={imgs.min()}, max={imgs.max()} ')
# print('coords:  ')
# print(f'     {type(coords)}')
# print(f'     {coords.shape}')
# print(f'     {coords.dtype}')

# class MyTransform(torch.nn.Module):
#     def forward(self, sample):
#         pass

class MyNormalize(torch.nn.Module):
    def __init__(self, mean, std):
        super().__init__()
        self.mean = mean
        self.std = std

    def forward(self, sample):
        sample = (sample - self.mean) / self.std
        return sample


class MyNormalize1:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, sample):
        sample = (sample - self.mean) / self.std
        return sample


transform = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Normalize(mean=(.5,), std=(.5,))
    ]
)

mytransform = transforms.Compose(
    [
        transforms.ToTensor(),
        MyNormalize(.5, .5)
    ]
)

mytransform1 = transforms.Compose(
    [
        transforms.ToTensor(),
        MyNormalize1(.5,.5)
    ]
)

img = Image.open(
    r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\dataset\img_0.jpeg')
img1 = transform(img)
print('img1: ')
print(f'     {type(img1)}')
print(f'     {img1.shape}')
print(f'     {img1.dtype}')
print(f'     min={img1.min()}, max={img1.max()} ')

img2 = mytransform(img)
print('img2: ')
print(f'     {type(img2)}')
print(f'     {img2.shape}')
print(f'     {img2.dtype}')
print(f'     min={img2.min()}, max={img2.max()} ')

img3 = mytransform1(img)
print('img3: ')
print(f'     {type(img3)}')
print(f'     {img3.shape}')
print(f'     {img3.dtype}')
print(f'     min={img3.min()}, max={img3.max()} ')

print(torch.equal(img1, img2))