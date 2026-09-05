import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.tensorboard import SummaryWriter


# TensorBoard logs save karne ke liye
writer = SummaryWriter("runs/experiment_1")


# Simple model
model = nn.Linear(1, 1)

# Learning rate
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Loss function
criterion = nn.MSELoss()


# Training data
# Hum model ko y = 2x + 1 seekha rahe hain
inputs = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
])

targets = torch.tensor([
    [3.0],
    [5.0],
    [7.0],
    [9.0],
])


# Training loop
for step in range(100):

    optimizer.zero_grad()

    # Forward pass
    outputs = model(inputs)

    # Calculate loss
    loss = criterion(outputs, targets)

    # Backward pass
    loss.backward()

    # Update weights
    optimizer.step()

    # TensorBoard mein loss save karo
    writer.add_scalar(
        "loss/train",
        loss.item(),
        step
    )

    # Learning rate bhi save karo
    writer.add_scalar(
        "learning_rate",
        optimizer.param_groups[0]["lr"],
        step
    )

    print(f"Step {step} | Loss: {loss.item():.4f}")


# Writer close
writer.close()

print("\n✅ Training complete!")
print("Run TensorBoard using:")
print("tensorboard --logdir=runs")
