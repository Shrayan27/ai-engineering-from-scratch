import torch
import torch.nn as nn
import torch.optim as optim


def detect_nan(model, loss, step):
    if torch.isnan(loss):
        print(f"\n🚨 NaN loss detected at step {step}")

        for name, param in model.named_parameters():
            if param.grad is not None:

                if torch.isnan(param.grad).any():
                    print(f"❌ NaN gradient in: {name}")

                if torch.isinf(param.grad).any():
                    print(f"❌ Inf gradient in: {name}")

        return True

    return False


# Simple model
model = nn.Linear(2, 1)

# Very high learning rate
optimizer = optim.SGD(model.parameters(), lr=10.0)

criterion = nn.MSELoss()

# Fake training data
inputs = torch.tensor([
    [1.0, 2.0],
    [2.0, 3.0],
])

targets = torch.tensor([
    [1.0],
    [2.0],
])


for step in range(100):

    optimizer.zero_grad()

    outputs = model(inputs)

    loss = criterion(outputs, targets)

    print(f"Step {step} | Loss: {loss.item()}")

    # Check before backward
    if detect_nan(model, loss, step):
        break

    loss.backward()

    # Check gradients
    if detect_nan(model, loss, step):
        break

    optimizer.step()
