import torch
t1 = torch.tensor(4.)
t2 = torch.tensor([2.,3,4,5])
t3 = torch.tensor([2.,3,4,5])


t4 = t1 * t2 + t3

print(t4)
