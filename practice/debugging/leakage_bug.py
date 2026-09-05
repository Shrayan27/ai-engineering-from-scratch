import pandas as pd


def check_data_leakage(train_set, test_set, id_column="id"):

    train_ids = set(train_set[id_column].tolist())
    test_ids = set(test_set[id_column].tolist())

    overlap = train_ids & test_ids

    if overlap:
        print(f"🚨 DATA LEAKAGE DETECTED!")
        print(f"Overlapping IDs: {overlap}")
        print(f"Total overlapping samples: {len(overlap)}")

        return True

    print("✅ No data leakage found!")

    return False


train_data = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "text": [
        "good movie",
        "bad movie",
        "excellent film",
        "boring film",
        "great movie"
    ]
})


test_data = pd.DataFrame({
    "id": [6, 7, 8, 9, 10],
    "text": [
        "boring film",
        "great movie",
        "average movie",
        "amazing movie",
        "terrible movie"
    ]
})


check_data_leakage(train_data, test_data)
