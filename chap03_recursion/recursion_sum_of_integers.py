def sum_first_num_normal(n):
    return n * (n + 1) // 2


def sum_first_num_recursive(n):
    if n == 0:
        # all of the calculation is actually based on this line!
        return 0

    # ↓ the order for pushing call frames ↓
    # 5 + { f(5-1) }
    #     4 + { f(4-1) }
    #         3 + { f(3-1) }
    #             2 + { f(2-1) }
    #                 1+ { f(1-1) } (0==0, base condition)
    # ↑ the order for calculating the returned values ↑

    # got the result then return (0->1->2 || 0 or n-1 MEETS 0)
    #              1+0
    #           2+(1+0)
    #         +(2+(1+0)))
    #     4+(3+(2+(1+0))))
    #  5+(4+(3+(2+(1+0)))))

    # note that the leftmost 4,3,2,1 above do NOT "exist" (VERIFY-NEEDED)
    #   they do not influence/being-included in the calculation
    #   they are merely the returned values
    #   they are the product of each returning (end-of-function)

    # PUSH the funcs onto the stack
    # POP  the funcs off  the stack once funcs weren't called anymore (==1)

    # my own explanation
    # > it follows LIFO operations
    # > stacked (fig & ds-type) functions won't change
    # > variable could change, therefore providing a 'base condition' (end/stp)

    # It's all about the RETURNED values, the former n does NOT matter
    return n + sum_first_num_recursive(n - 1)


# references
#   concept with examples
#       https://dev.to/kaxmoglan/recursive-functions-explained-5hie


def main():
    _input = int(input("Enter a non-negative and non-zero integer: "))

    print(
        sum_first_num_normal(_input), sum_first_num_recursive(_input), sep="\n"
    )


if __name__ == "__main__":
    main()
