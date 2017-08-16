# Foobar Level 2, Challenge 2.

def answer(xs):
    # Notably, in Python 2.5 and beyond, large numbers are already supported
    # without need to cast them to a string.
    positives = [num for num in xs if num>0]
    negatives = [num for num in xs if num<0]
    npos = len(positives)
    nneg = len(negatives)
    energy = 1
    # This captures the case where we have a single negative number, or only a zero.
    # It may not capture the case where we have a negative number and then a string of zeroes.
    if (npos == 0 and nneg == 1) or (npos == 0 and nneg == 0):
        return xs[0]
    # Case: No positive numbers.
    elif npos == 0:
        # If we have an odd number of negative numbers, we need to remove the largest.
        if nneg%2 == 1:
            negatives.remove(max(negatives))
            nneg -= 1
        for num in negatives:
            energy *= num
        return energy
    # Case: No negative numbers or one negative number.
    elif nneg == 0 or nneg == 1:
        for num in positives:
            energy *= num
        return energy
    # Case: Multiple positive and negative numbers.
    else:
        if nneg%2 == 1:
            negatives.remove(max(negatives))
        for num in positives:
            energy *= num
        if nneg > 0:
            for num in negatives:
                energy *= num
        return energy


if __name__ == "__main__":
    case0 = [2, 0, 2, 2, 0]
    print("\nCase 0:\n ", case0, "\n\n  Expected: 8\nCalculated:", answer(case0))

    case1 = [-2, -3, 4, -5]
    print("\nCase 1:\n ", case1, "\n\n  Expected: 60\nCalculated:", answer(case1))

    case2 = [0, 0, 0, -43]
    print("\nCase 2:\n ", case2, "\n\n  Expected: -43\nCalculated:", answer(case2))

    case3 = [0, 0]
    print("\nCase 3:\n ", case3, "\n\n  Expected: 0\nCalculated:", answer(case3))

    case4 = [0, 0, 4]
    print("\nCase 4:\n ", case4, "\n\n  Expected: 4\nCalculated:", answer(case4))

    case5 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
    print("\nCase 5:\n ", case5, "\n\n  Expected: 1000000000000000000000000000000000000000000000000000000\
    \nCalculated:", answer(case5))

