from datasets import load_dataset

print("Loading GLUE MRPC dataset...\n")

# Load dataset
dataset = load_dataset(
    "nyu-mll/glue",
    "mrpc",
    split="train"
)

print(f"Original dataset size: {len(dataset)}")

# Step 1: Separate 30% for validation + test
first_split = dataset.train_test_split(
    test_size=0.30,
    seed=42
)

train_ds = first_split["train"]
remaining_ds = first_split["test"]

# Step 2: Split remaining 30% equally
# 15% validation + 15% test
second_split = remaining_ds.train_test_split(
    test_size=0.50,
    seed=42
)

val_ds = second_split["train"]
test_ds = second_split["test"]

# Print results
print("\n" + "=" * 40)
print("70 / 15 / 15 DATA SPLIT")
print("=" * 40)

print(f"Train:      {len(train_ds)} examples")
print(f"Validation: {len(val_ds)} examples")
print(f"Test:       {len(test_ds)} examples")

total = len(train_ds) + len(val_ds) + len(test_ds)

print("\n" + "=" * 40)
print(f"Total after split: {total}")

print("\nPercentages:")
print(f"Train:      {len(train_ds) / total * 100:.2f}%")
print(f"Validation: {len(val_ds) / total * 100:.2f}%")
print(f"Test:       {len(test_ds) / total * 100:.2f}%")

print("\nSeed used: 42")
print("✅ Exercise 4 completed successfully!")
