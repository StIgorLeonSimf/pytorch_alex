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

p = r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\img.png'
plt.axis('off')
plt.imshow(Image.open(p))
plt.show()

img = np.array(Image.open(p))
print(type(img))
print(img.shape)
print(img.dtype)
print(f' min = {img.min()}, max = {img.max()}')
# изображение преобразуем в тензор
# (H, W, C) -> (C, H, W)
# (0, 255) -> (0.0, 1.0)
transform = transforms.ToTensor()
img_totensor = transform(img)
print(type(img_totensor))
print(img_totensor.shape)
print(img_totensor.dtype)
print(f' min = {img_totensor.min()}, max = {img_totensor.max()}')

# нормализация
# transform = transforms.Normalize(mean=( 0.5, 0.5, 0.5),
#                                  std=(0.5, 0.5, 0.5))
# img_norm = transform(img_totensor)
# print(type(img_norm))
# print(img_norm.shape)
# print(img_norm.dtype)
# print(f' min = {img_norm.min()}, max = {img_norm.max()}')
#
transform = transforms.Compose(
    [transforms.Lambda(lambda img: img.convert('RGB')),
     transforms.ToTensor(),
     transforms.Normalize(mean=(0.5, 0.5, 0.5),
                          std=(0.5, 0.5, 0.5))
     ]
)
print('Сompose')
img = transform(Image.open(p))
print(type(img))
print(img.shape)
print(img.dtype)
print(f' min = {img.min()}, max = {img.max()}')

# преобразования при помощи v2
print('\nпреобразования при помощи v2\n')
transform = v2.ToImage()
img_v2 = transform(Image.open(p))
print(type(img_v2))
print(img_v2.shape)
print(img_v2.dtype)
print(f' min = {img_v2.min()}, max = {img_v2.max()}')
# изменение типа данных
# transform = v2.ToDtype(torch.float32, scale=True)
# img_dtype_v2 = transform(img_v2)
# img_dtype_v2 = img_dtype_v2[:3] if img_dtype_v2.shape[0] == 4 else img_dtype_v2  # 3. Убираем альфа
# print(type(img_dtype_v2))
# print(img_dtype_v2.shape)
# print(img_dtype_v2.dtype)
# print(f' min = {img_dtype_v2.min()}, max = {img_dtype_v2.max()}')

transform = v2.Compose(
    [transforms.ToTensor(),
     v2.ToDtype(torch.float32, scale=True),
     v2.Lambda(lambda x: x[:3] if x.shape[0] == 4 else x),  # Убираем альфа
     v2.Normalize(mean=(0.5, 0.5, 0.5),
                  std=(0.5, 0.5, 0.5))

     ]
)
# v2.Lambda(lambda x: x[:3] if x.shape[0] == 4 else x),  # Убираем альфа
img = transform(Image.open(p))
print(type(img))
print(img.shape)
print(img.dtype)
print(f' min = {img.min()}, max = {img.max()}')
