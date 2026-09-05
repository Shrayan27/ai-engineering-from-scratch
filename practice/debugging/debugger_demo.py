import torch


def calculate_loss(prediction, target):
    error = prediction - target
    squared_error = error ** 2
    loss = squared_error.mean()

    return loss


predictions = torch.tensor([2.0, 4.0, 6.0])
targets = torch.tensor([3.0, 5.0, 7.0])

loss = calculate_loss(predictions, targets)

print("Loss:", loss.item())
