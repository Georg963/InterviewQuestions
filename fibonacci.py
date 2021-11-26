def fib(x: int) -> int:
    if x <= 0:
        return 1
    return x * fib(x-1)

print(f"3! = 3 * 2 * 1 = {fib(3)}") #6
print(f"4! = 4 * 3 * 2 * 1 = {fib(4)}") #24