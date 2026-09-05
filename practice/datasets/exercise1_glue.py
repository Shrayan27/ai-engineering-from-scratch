from datasets import load_dataset

print("Loading GLUE MRPC dataset...\n")

dataset = load_dataset(
    "nyu-mll/glue",
    "mrpc",
)

print(dataset)

print("\nFirst 5 training examples:\n")

for i in range(5):
    example = dataset["train"][i]

    print(f"Example {i + 1}")
    print("Sentence 1:", example["sentence1"])
    print("Sentence 2:", example["sentence2"])
    print("Label:", example["label"])
    print("-" * 50)