import time


@profile
def train_step():
    numbers = list(range(1_000_000))

    total = sum(numbers)

    time.sleep(1)

    return total


train_step()
