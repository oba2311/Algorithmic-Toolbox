# python3


def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False


def gcd(a, b):
    """
    every iteration, take the numbers given and
    if those aren't strictly divided with no remainder (this is
    the stopping condition), figure the minimal one
     and the remainder recursively
    until stopping condition is met.
    """
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9
    if a % b == 0 or b % a ==0:
        return min(a, b)
    mi, ma = min(a, b), max(a, b)
    new_num, remainder = int(mi), ma % mi
    return gcd(new_num, remainder)







if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
