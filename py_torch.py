import torch
import numpy as np

# tensor = torch.tensor([2, 3])
# tensor = torch.tensor([[2, 3], [4, 5]], dtype=torch.float32)
"""tensor = torch.tensor([[2, 3], [4, 5]], dtype=torch.int32,
                      requires_grad=True)"""
# tensor = torch.tensor([[2, 3], [4, 5]], dtype=torch.float32,
#                       requires_grad=True)
# tensor = torch.tensor([[2, 3], [4, 5]], dtype=torch.float32,
#                       requires_grad=True, device=torch.device('cuda:0'))

# print(tensor, tensor.dtype)
# print(torch.cuda.is_available())
tensor = torch.tensor([[[2, 3], [4, 5]], [[6, 7], [8, 9]]],
                      dtype=torch.float32, requires_grad=True)
# print(tensor)
# print(tensor.dtype)
# print(tensor.shape)
# print(tensor.size())
# print(tensor.ndim)
# print(tensor[0, 0, 0])
# print(type(tensor[0, 0, 0]))
# print(tensor[0, 0, 0].item())
# print(type(tensor[0, 0, 0].item()))

# tens = torch.zeros([2, 3, 2])
tens = torch.ones([3, 3])
# tens = torch.zeros_like(tens)
# tens = torch.full_like(tens, 7)
# tens = torch.arange(2.2, 10.5, .5)
# tens = np.arange(2.2, 10.5, .5)
# tens = torch.diag(torch.tensor([5, 4]))
# tens = torch.eye(5)
# tens = torch.tril(torch.tensor([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))
tens = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
tens_1 = tens.view(4, 1)
# tens_2 = tens.reshape([2, 2])
# print(tens_1)
# tens = torch.unsqueeze(tens_2, 0)
# print(tens.shape)
# print(tens * 5)
# def power(n):
#     return n * n

# print(power(tens))

# print(tens.sum())
# print(tens.sum().item())
# print(tens.mean())

# tens = torch.tensor([1, 2, 3, 4, 5, 6], dtype=torch.float32)
# tens = tens.view([2, 3])
# print(tens)
# tens_mean = tens.mean(dim=1, keepdim=True)
# print(tens_mean)

"""CPU GPU"""

print(torch.cpu.is_available())
print(torch.cuda.is_available())

tens = tens.cpu()
tens = tens.to('cpu')

"""
tens = tens.cuda()
tens = tens.to('cuda')
"""
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tensor = tensor.to(device)
new_tens = tens + tens_1  # тензоры должны быть на одном устройстве
new_tens = tens + tens_1.to(device)  # тензоры должны быть на одном устройстве

new_tens = new_tens.cpu().detach()