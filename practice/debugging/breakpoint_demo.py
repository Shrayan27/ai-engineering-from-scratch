import torch


def training_step():
    inputs = torch.tensor([1.0, 2.0, 3.0])
    outputs = inputs * 10

    print("Before breakpoint")

    breakpoint()

    print("After breakpoint")
    print("Outputs:", outputs)


training_step()
