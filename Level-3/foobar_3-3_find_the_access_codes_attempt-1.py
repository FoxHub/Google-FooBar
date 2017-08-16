# Foobar Level 3, Challenge 3, Attempt 1.

triplets = 0


def seek_multiples(l, num, tier, iter):
    if l == []:
        return
    if tier == 1:
        multiples = range(num, max(l)+1, num)
        for potentialmult in l:
            iter += 1
            if potentialmult in multiples:
                seek_multiples(l[iter:], potentialmult, tier+1, iter)
    elif tier == 2:
        multiples = range(num, max(l)+1, num)
        for potentialtriplet in l:
            if potentialtriplet in multiples:
                global triplets
                triplets += 1
    else:
        return


def answer(l):
    """
    There are a lot of things wrong with this solution. Make it a game to spot them!

    :param l: A list of integers to be evaluated.
    :return: The number of 'lucky triplets' in the given list.
    """
    global triplets
    triplets = 0
    if len(l) < 3:
        # impossible to have triplets
        return 0
    iter = 0
    for num in l:
        iter += 1
        seek_multiples(l[iter:], num, 1, iter)
    return triplets


if __name__ == '__main__':
    case0 = [1, 1, 1]
    print("\nCase 0:\n", case0, "\n\n  Expected: 1\nCalculated:", str(answer(case0)))

    case1 = [1, 2, 3, 4, 5, 6]
    print("\nCase 1:\n", case1, "\n\n  Expected: 3\nCalculated:", str(answer(case1)))

    case2 = [1, 2, 4, 8]
    print("\nCase 2:\n", case2, "\n\n  Expected: 4\nCalculated:", str(answer(case2)))