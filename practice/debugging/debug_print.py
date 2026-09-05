import torch


def debug_print(name, tensor):
    print(
        f"{name}: "
        f"shape={tensor.shape}, "
        f"dtype={tensor.dtype}, "
        f"device={tensor.device}, "
        f"min={tensor.min().item():.4f}, "
        f"max={tensor.max().item():.4f}, "
        f"mean={tensor.mean().item():.4f}, "
        f"has_nan={tensor.isnan().any().item()}"
    )


x = torch.tensor([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
])

debug_print("Input Tensor", x)
