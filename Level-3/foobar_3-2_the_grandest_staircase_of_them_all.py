# Foobar Level 3, Challenge 2.

# Given N bricks, we have to construct M staircases, where the height of each pile of bricks always decreases
# by at least 1 moving left to right.
# By definition, you cannot build any staircase out of 0, 1, or 2 bricks, so we return 0 in those cases.

# This problem is also notably known as Euler's distinct partition problem, which I read about here:
#     https://en.wikipedia.org/wiki/Partition_(number_theory)
# We solve that as we'd otherwise solve the distinct partition problem, with one curve ball: we do not
# count the partition where all the bricks are in a single partition. To account for this, we only need
# to count 1 less than the entire answer to the distinct partitions problem.

# Since the number of odd partitions is always equal to the number of distinct partitions, we could also solve this
# problem by solving for the number of odd partitions that can be used to construct a staircase out of n bricks.


def answer(n):
    combinations = [[0 for rows in range(n)] for cols in range(n + 1)]

    # If n < 3, there are no possibilities for building the stairwell.
    for first_three in range(3):
        for num in range(first_three, n):
            combinations[first_three][num] = 1

    # For the rest of them, the formula is incremental.
    for num in range(3, n + 1):
        for bot in range(2, n):
            combinations[num][bot] = combinations[num][bot - 1]
            if bot <= num:
                combinations[num][bot] += combinations[num - bot][bot - 1]

    # This index on the matrix should contain our solution to the number of distinct combinations.
    return combinations[n][n - 1]


if __name__ == '__main__':
    # This prints out the results of this function on any value between (including) 3 and 200.
    # It's just for debugging.
    print("Format:\n Number of Bricks --> Distinct Partitions")
    for bricks in range(3, 200):
        print('   ', bricks, " --> ", str(answer(bricks)))

