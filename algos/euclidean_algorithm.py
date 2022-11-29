"""
Find the greatest common denominator between two numbers.
https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
"""

def get_greatest_common_denominator(num1: int, num2: int) -> int:
    """Uses Euclidean algorithm to get greatest common denominator."""
    if num1 == 0: return num2
    if num2 == 0: return num1

    greater_num, lesser_num = (num1, num2) if num1 >= num2 else (num2, num1)
    remainder = greater_num % lesser_num

    if remainder == 0:
        return lesser_num

    return get_greatest_common_denominator(lesser_num, remainder)


def main() -> None:
    test_cases = [
        [(1, 2), 1],
        [(2, 1), 1],
        [(210, 45), 15],
        [(18, 6), 6],
        [(60, 0), 60],
        [(10, 15), 5],
    ]
    for case in test_cases:
        gcd = get_greatest_common_denominator(*case[0])
        if gcd != case[1]:
            print("Expected {}, but got {}".format(case[1], gcd))


if __name__ == '__main__':
    main()
