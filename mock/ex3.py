from typing import Iterator


def dividers(n: int) -> int:
    output = []
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"zoznam verzia {i}")
            output.append(i)

    return output


def dividers2(n: int) -> Iterator[int]:
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"generator {i}")
            yield i


#dividers(6)

for i in dividers(6):
    print(i)