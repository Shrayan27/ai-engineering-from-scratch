import torch


if torch.cuda.is_available():

    print(torch.cuda.memory_summary())

    print(
        f"Allocated: "
        f"{torch.cuda.memory_allocated() / 1e9:.2f} GB"
    )

    print(
        f"Reserved: "
        f"{torch.cuda.memory_reserved() / 1e9:.2f} GB"
    )

else:
    print("CUDA GPU is not available on this system.")
    print("GPU memory profiling skipped.")
