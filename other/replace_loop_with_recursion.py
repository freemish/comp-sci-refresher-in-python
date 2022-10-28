"""Demonstrates a way of replacing any loop with recursion."""


def loop_example() -> int:
    x = 0
    while x < 12:
        x += 1
    return x


def recursion_example(x: int = 0) -> int:
    if x >= 12:
        return x
    return recursion_example(x+1)


def recursion_example_without_default() -> int:
    x = 0

    def recurrently_add_one_until_12(i) -> int:
        if i >= 12:
            return i
        return recurrently_add_one_until_12(i+1)
    
    return recurrently_add_one_until_12(x)


def main() -> None:
    loop_x = loop_example()
    recursion_x = recursion_example()
    purecursion_x = recursion_example_without_default()

    assert loop_x == recursion_x == purecursion_x == 12
    print(loop_x)


if __name__ == '__main__':
    main()


"""
$python3 other/replace_loop_with_recursion.py
12
"""
