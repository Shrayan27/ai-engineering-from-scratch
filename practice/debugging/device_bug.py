import torch
import torch.nn as nn


def check_devices(model, *tensors):

    model_device = next(model.parameters()).device

    print(f"Model device: {model_device}")

    for i, tensor in enumerate(tensors):

        print(f"Tensor {i} device: {tensor.device}")

        if tensor.device != model_device:

            print(
                f"⚠️ WARNING: Tensor {i} is on "
                f"{tensor.device}, but model is on {model_device}"
            )

        else:
            print(f"✅ Tensor {i} is on the correct device")


# Automatically select GPU if available
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print(f"Using device: {device}\n")


# Create model
model = nn.Linear(3, 2)

# Move model to device
model = model.to(device)


# Input tensor
inputs = torch.randn(5, 3)

# Check devices
check_devices(model, inputs)


# Correct way:
inputs = inputs.to(device)

print("\nAfter moving input:")

check_devices(model, inputs)


# Run model
output = model(inputs)

print("\nOutput shape:", output.shape)
print("Output device:", output.device)
