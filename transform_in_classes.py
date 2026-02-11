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

transform = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5,), std=(0.5,))
    ]
)

train_data = MnistDataset(r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\training')
test_data = MnistDataset(r'D:\UNITS\Python\Units\ALEX_VELIEVS_PYTORCH\data\MNIST\testing')