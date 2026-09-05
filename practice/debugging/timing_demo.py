import time


class Timer:
    def __init__(self, name=""):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        elapsed = time.perf_counter() - self.start
        print(f"[{self.name}] {elapsed:.4f} seconds")


with Timer("Fast operation"):
    total = sum(range(1_000_000))


with Timer("Slow operation"):
    time.sleep(2)


print("Total:", total)
