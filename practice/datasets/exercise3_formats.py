from datasets import load_dataset
import os

print("Loading GLUE MRPC dataset...\n")

# Load the training dataset
dataset = load_dataset(
    "nyu-mll/glue",
    "mrpc",
    split="train"
)

print(f"Total examples: {len(dataset)}")

# Use a maximum of 1000 examples
subset_size = min(1000, len(dataset))
dataset = dataset.select(range(subset_size))

print(f"Using {len(dataset)} examples for comparison...\n")

# File paths
csv_file = "mrpc.csv"
parquet_file = "mrpc.parquet"

# Save as CSV
print("Saving dataset as CSV...")
dataset.to_csv(csv_file)

# Save as Parquet
print("Saving dataset as Parquet...")
dataset.to_parquet(parquet_file)

# Get file sizes
csv_size = os.path.getsize(csv_file)
parquet_size = os.path.getsize(parquet_file)

print("\n" + "=" * 40)
print("FILE SIZE COMPARISON")
print("=" * 40)

print(f"CSV size:     {csv_size / 1024:.2f} KB")
print(f"Parquet size: {parquet_size / 1024:.2f} KB")

difference = csv_size - parquet_size

print(f"Difference:   {abs(difference) / 1024:.2f} KB")

if parquet_size < csv_size:
    print("\n✅ Parquet is smaller!")
else:
    print("\n📄 CSV is smaller for this dataset.")

print("\nExercise 3 completed successfully! 🎉")

