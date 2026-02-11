import os
import json
import random
import struct
import sys
from array import array
from os import path
import torchvision
import numpy as np
from PIL import Image

# # train_dataset = torchvision.datasets.MNIST(
# #     root=r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data',
# #     train=True, download=True)
#
#
# def read(dataset):
#     if dataset == 'training':
#         path_img = r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\raw\train-images-idx3-ubyte'
#         path_lbl = r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\raw\train-labels-idx1-ubyte'
#     elif dataset == 'testing':
#         path_img = r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\raw\t10k-images-idx3-ubyte'
#         path_lbl = r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\raw\t10k-labels-idx1-ubyte'
#     else:
#         raise ValueError('набор должен быть "testing" или "train" ')
#
#     with open(path_lbl, 'rb') as f_lable:
#         _, size = struct.unpack(">II", f_lable.read(8))
#         lbl = array('b', f_lable.read())
#     with open(path_img, 'rb') as f_img:
#         _, size, rows, cols = struct.unpack('>IIII', f_img.read(16))
#         img = array('B', f_img.read())
#     return lbl, img, size, rows, cols
#
#
# def write_dataset(labels, data, size, rows, cols, output_dir):
#     classes = {i: f'class_{i}' for i in range(10)}
#     output_dirs = [path.join(output_dir, classes[i]) for i in range(10)]
#     for dir in output_dirs:
#         # if not path.exists(dir):
#         #     os.makedirs(dir)
#         os.makedirs(dir, exist_ok=True)
#     # запись в папки
#     for i, label in enumerate(labels):
#         output_filename = path.join(output_dirs[label],
#                                     str(i) + '.jpg')
#         print('writing ' + output_filename)
#         with open(output_filename, 'wb') as h:
#             data_i = [
#                 data[(i * rows * cols + j * cols):
#                      (i * rows * cols + (j + 1) * cols)]
#                 for j in range(rows)
#             ]
#             data_array = np.array(data_i)
#             im = Image.fromarray(data_array)
#             im.save(output_filename)
#
#
# output_path = r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\mnist'
# for dataset in ['training', 'testing']:
#     write_dataset(*read(dataset), path.join(output_path, dataset))


os.makedirs('data/dataset', exist_ok=True)
img = np.random.randint(0, 50, [100000, 64, 64], dtype=np.uint8)
square = np.random.randint(100, 200, [100000, 15, 15], dtype=np.uint8)
coords = np.empty([100000, 2])

data = {}
for i in range(img.shape[0]):
    x = np.random.randint(20, 44)
    y = np.random.randint(20, 44)
    img[i, (y-7):(y+8), (x-7):(x+8)] = square[i]
    coords[i] = [y, x]
    name_img = f'img_{i}.jpeg'
    path_img = os.path.join('data/dataset', name_img)
    image = Image.fromarray(img[i])
    image.save(path_img)
    data[name_img] = [y, x]
    # p = r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\
with open('data/dataset/coords.json', 'w') as f:
    json.dump(data, f)  # indent=2






# arr = random.sample(range(10, 99), 24)
# arr = np.array(arr)
# arr = arr.reshape(4, 6)
# print(arr)
# print(arr[1, 2])
# arr[1, 2] = 99
# print(arr[1, 2])
# arr[1:3, 2:4] = np.array([[11, 12], [21, 22]])
# print(arr)
