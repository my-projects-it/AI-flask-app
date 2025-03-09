#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install torch')


# In[2]:


import torch
import torch.nn as nn
import torch.optim as optim

class RM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RM, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):  # Changed 'f' to 'forward'
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Model, loss function, and optimizer
model = RM(10, 20, 5)
criterion = nn.MSELoss()  # Changed variable 'c' to 'criterion' for clarity
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training function
def train(data, target):
    optimizer.zero_grad()
    data = torch.tensor(data, dtype=torch.float32)  # Ensure it's a tensor
    target = torch.tensor(target, dtype=torch.float32)  # Ensure it's a tensor
    output = model(data)  # Calls the 'forward()' method automatically
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()
    print(f"Loss: {loss.item()}")
    return loss.item()  # Return loss for monitoring


# In[3]:


import numpy as np
# Generate random input and target data
data = np.random.rand(1, 10)  # 1 sample, 10 features
target = np.random.rand(1, 5)  # 1 sample, 5 target values
for epoch in range(5):
    print(f"Epoch {epoch+1}:")
    train(data, target) 


# In[ ]:




