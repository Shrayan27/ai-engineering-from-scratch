from datasets import load_dataset
import time

print("Starting C4 streaming...\n")

dataset = load_dataset(
    "allenai/c4",
    "en",
    split="train",
    streaming=True,
)

start_time = time.time()
count = 0

for example in dataset:
    count += 1

    if time.time() - start_time >= 10:
        break

print(f"\nExamples processsed in 10 seconds: {count}")
