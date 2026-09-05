import time


def fast_function():
    total = sum(range(100_000))
    return total


def slow_function():
    time.sleep(1)


def main():
    fast_function()
    slow_function()


main()
