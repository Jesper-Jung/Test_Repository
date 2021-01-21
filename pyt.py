import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

m = nn.linear(20, 20)

input = torch.tensor(np.ones((50, 20))).float()
output = m(input)
print(output.shape)