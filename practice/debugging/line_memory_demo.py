from memory_profiler import profile


@profile
def load_data():
    print("Creating first dataset...")

    raw_data = list(range(2_000_000))

    print("Creating processed dataset...")

    processed_data = [x * 2 for x in raw_data]

    return processed_data


data = load_data()

print("Data created successfully")
