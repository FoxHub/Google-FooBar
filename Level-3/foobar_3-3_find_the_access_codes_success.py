# Foobar Level 3, Challenge 3, Attempt 2.

# Looking at attempt 1, it's clear that my naive but correct solution was O(n^3). However, the following
# shorter, simple refinement should be only O(n^2), which I believe is the minimum time required
# for this algorithm, since we simply must evaluate elements in the array at least twice.


def answer(l):
    """
    We start by initializing a counter for every number in the list.
    This counter resembles the number of times a particular entry in the list has been a multiple of a previous number.
    Each time we increment that, we can also increase our number of triplets by the factor we're currently evaluating.

    For example:
    [1, 2, 4, 8]

    When we reach 2, 1 is obviously a factor of 2. c[2] = 1.
    When we reach 4, 1 is a factor of 4. c[4] = 1.
                     2 is a factor of 4. c[4] = 2. triplets += c[2] (triplets is now 1)
    When we reach 8, 1 is a factor of 8. c[8] = 1.
                     2 is a factor of 8. c[8] = 2. triplets += c[2] (triplets is now 2)
                     4 is a factor of 8. c[8] = 3. triplets += c[4]. (triplets is now 4)

    :param l: A list of integers to be evaluated.
    :return: The number of 'lucky triplets' in the given list.
    """
    counts = [0] * len(l)
    triplets = 0
    for product in range(0, len(l)):
        for factor in range(0, product):
            if l[product] % l[factor] == 0:
                counts[product] += 1
                triplets += counts[factor]
    return triplets

if __name__ == '__main__':
    case0 = [1, 1, 1]
    print("\nCase 0:\n", case0, "\n\n  Expected: 1\nCalculated:", str(answer(case0)))

    case1 = [1, 2, 3, 4, 5, 6]
    print("\nCase 1:\n", case1, "\n\n  Expected: 3\nCalculated:", str(answer(case1)))

    case2 = [1, 2, 4, 8]
    print("\nCase 2:\n", case2, "\n\n  Expected: 4\nCalculated:", str(answer(case2)))

