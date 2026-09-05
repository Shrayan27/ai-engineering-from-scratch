import tracemalloc


tracemalloc.start()


def create_data():
    numbers = list(range(1_000_000))
    return numbers


data = create_data()


snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")


print("\nTop memory usage:\n")

for stat in top_stats[:10]:
    print(stat)
