memo = {}  # a set


def fib(n):
    """
    Complexity: O(n)
    Enhanced version of fib (WAY FASTER than the original one).
    """

    if n in memo:
        return memo[n]

    if n == 0:
        memo[0] = 0
        return 0

    if n == 1:
        memo[1] = 1
        return 1

    val = fib(n - 1) + fib(n - 2)
    memo[n] = val

    return val


def main() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55

    # Here's the stats if not using memoizations:
    # > TIME: 363,000,000 years
    # > CALL: 1,146,295,688,027,634,168,201 calls
    assert fib(100) == 354224848179261915075  # 10ms, with memoizations

    # 🤷
    fib_900 = int(
        (
            "548771088394800000514136739483837144438"
            "005193091235927244949534270398112010643"
            "412349543875215253906155049490921874412"
            "182466791047314424730220139801604070070"
            "17175697317900483275246652938800"
        )
    )
    assert fib(900) == fib_900


if "__main__" == __name__:
    main()
