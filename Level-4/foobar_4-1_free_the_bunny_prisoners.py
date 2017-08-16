# To me, this appears to be a classic combinations problem. This makes sense, given previous questions were also based
# upon mathematical theories.

# So another way of looking at this problem... is to word it like this:
# If you have N bunnies, and M locks, distribute M distinct keys among the bunnies so that it will always require
# num_required bunnies to open the locks.

# Another property of this: There should be M copies of each distinct key among the bunnies, and no bunny should have
# the same key twice.

# Thus, for the example of N = 5 and M = 3, there are 5 choose 3 distinct keys (10 keys).
# We must distribute copies of all 10 keys amongst the bunnies in such a way that any 3 bunnies we pair together have,
# amongst them, at least one copy of every key.

from itertools import combinations
# Thankfully, combinations are in the Python standard library, according to a quick Google search.


def answer(num_buns, num_required):
    """
    To start this problem, we calculate the number of ways we can arrange bunnies. This is:
        num_buns choose num_required

    This number determines how many distinct keys we have. So we then need to lexicographically hand off keys to each
    bunny and deputize them with the powers to open locks.

    At that point, this problem comes down to deciding how many keys to hand to each bunny. I had to think about that
    by hand.

    :param num_buns: The number of bunnies to distribute keys to.
    :param num_required: The "choose" part of our combinatorial.
    :return: bunny_keyrings, the enumerated keys belonging to each bunny in num_buns.
    """
    # One keyring per bunny.
    bunny_keyrings = [[] for num in range(num_buns)]
    # The number of keys each bunny requires is described by this formula, which I noticed by doing some napkin math.
    # If N == 4 and M == 4, bunnies_per_key == 1.
    # If N == 2 and M == 1, bunnies_per_key == 2.
    # If N == 5 and M == 3, bunnies_per_key == 3.
    # This generally fit the formula bunnies_per_key = N - M + 1.
    bunnies_per_key = num_buns - num_required + 1

    # itertools' enumerate function:
    # def enumerate(sequence, start=0):
    #     n = start
    #     for elem in sequence:
    #         yield n, elem
    #         n += 1
    # This yields a generator! So by generating combinations one at a time, we will get num_buns choose num_required
    # different permutations of num_buns, and we can assign each one as a bunny's keyring. Since this covers all
    # combinations, it should also assure that in all situations, if we pick num_required bunnies, they will all have
    # enough keys to open a cell.
    for keynum, keyholders in enumerate(combinations(range(num_buns), bunnies_per_key)):
        # print(keynum, keyholders)
        for index in keyholders:
            bunny_keyrings[index].append(keynum)

    return bunny_keyrings


if __name__ == '__main__':
    case0 = [2, 1]
    print(case0, " --> ", str(answer(case0[0], case0[1])))
    case1 = [5, 3]
    print(case1, " --> ", str(answer(case1[0], case1[1])))
    case2 = [4, 4]
    print(case2, " --> ", str(answer(case2[0], case2[1])))

