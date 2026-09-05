import torch
import torch.nn as nn


model = nn.Linear(3, 2)

# Model expects 3 features
wrong_input = torch.tensor([
    [1.0, 2.0]
])

output = model(wrong_input)

print("Correct input shape:", correct_input.shape)

output = model(correct_input)

print("Output shape:", output.shape)
print("Output:", output)
