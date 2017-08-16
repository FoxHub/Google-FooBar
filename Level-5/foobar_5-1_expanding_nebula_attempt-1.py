import json

"""
The Algorithm
-------------

- We are building all potential preimages for a NxM boolean matrix.
- Start at [0, 0]. Pick a potential starting column for the pre-image from [0, 0], [0, 1], [1, 0], [1, 1]].
- Build logic trees to create all potential combinations of the first row by analyzing the current image state.
    • Do this by: 
        1) Calculate the sum of the previous 1x2 column.
        2) Try all combinations in our dictionary that correspond to the sum and our desired state.
        3) Treat our most recent column as the previous column, returning to step 1.
        4) At the end of the row, use the logic tree to construct the bottom row of our resulting Nx2 matrix.
- ... Do something with the row.
"""

count = 0

# This table will act as a list of columns to append in the first step of my algorithm: Constructing the first row.
soltable = [
    # Index 0: When the previous column or row's sum is 0. [0, 0]
    {
        0: [[0, 0], [1, 1]],
        1: [[1, 0], [0, 1]]
    },
    # Index 1: "" is 1. [0, 1], [1, 0]
    {
        0: [[0, 1], [1, 0], [1, 1]],
        1: [[0, 0]]
    },
    # Index 2: "" is 2. [1, 1]
    {
        0: [[0, 0], [0, 1], [1, 0], [1, 1]],
        1: None
    }
]

unitsoltable = [
    # Index 0: When the previous column or row's sum is 0. [0, 0, 0]
    {
        0: [0],
        1: [1]
    },
    # Index 1: "" is 1. [0, 0, 1], [0, 1, 0], [1, 0, 0]
    {
        0: [1],
        1: [0]
    },
    # Index 2: "" is 2. [0, 1, 1], [1, 0, 1], [1, 1, 0]
    {
        0: [0, 1],
        1: None
    },
    # Index 3: "" is 3. [1, 1, 1]
    {
        0: [0, 1],
        1: None
    }
]


def bool_to_int(matrix):
    """
    I find it much easier to read 0s and 1s than boolean words, so I wrote this helper function.

    :param matrix: A matrix to translate to integers.
    :return: A matrix of integers.
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = int(matrix[row][col])
    return matrix


# @profile
def fill_preimages(above, image, depth):
    """
    This recursive function takes a slightly different approach. Looking only at the row directly above us,
    this recursive function chooses a random first element of the row we're generating, and then moves from there to
    create any possible images.

    :param above: The row above the one we're generating. Our "roof".
    :param image: The image we're building a preimage for.
    :param depth: How many levels deep we've generated rows.
    :return: Nothing.
    """

    if depth >= len(image):
        # This is the case we're working up to! If we've reached this point, we've created a series of valid logic tree
        # decisions that has led us to a complete preimage. We increment our counter by 1, and return.
        # print("Incrementing count.")
        # print("Solution:\n", above)
        global count
        count += 1
        return

    for state in [0, 1]:
        row = [state]
        generate_row(row, tuple(above), image, depth)


# @profile
def generate_first_row(prevcols, firstrows, image):
    """
    This recursive function uses the soltable above to construct all possible configurations of the first
    row of each solution matrix.

    :param prevcols: The column preceding the column being generated on this iteration.
    :param firstrows: Upon first invocation, this should be an empty list.
    :param image: The current image matrix.
    :return: A list of all feasible first rows for our preimage matrices.
    """

    if len(prevcols[0]) > len(image[0]):
        # print("Found potential first row. Returning:\n", prevcols[0], "\n", prevcols[1])
        firstrows.append(prevcols)
        return
    end = len(prevcols[0])-1
    prevsum = prevcols[0][end] + prevcols[1][end]
    # Look up the potential columns in our solution table based on the image state we're looking for.
    potentialcols = soltable[prevsum][image[0][len(prevcols[0])-1]]
    # print("Index {}; seeking 1:".format(prevsum), soltable[prevsum][1])
    if potentialcols is None:
        # print("Seeking 1 and sum is 2 or higher. Leave.")
        # print(prevcols)
        return
    for col in potentialcols:
        temp = json.loads(json.dumps(prevcols))
        temp[0].append(col[0])
        temp[1].append(col[1])
        generate_first_row(temp, firstrows, image)
    return firstrows


# @profile
def generate_row(prev, above, image, depth):
    length = len(prev)-1
    # height = len(above)-1
    if length+1 == len(above):
        # print("Potential row:", prev)
        # temp = cPickle.loads(above)
        # temp.append(prev)
        fill_preimages(prev, image, depth+1)
        return
    prevsum = above[length] + above[length + 1] + prev[length]
    possibilities = unitsoltable[prevsum][image[depth][length]]
    # print(above, prev, prevsum, depth)
    try:
        for poss in possibilities:
            temp = prev[:]
            temp.append(poss)
            generate_row(temp, above, image, depth)
    except TypeError:
        # If our sum is already too high to generate a 1 (it's 2 or 3),
        # then we return. Processing further is impossible.
        return


# @profile
def generate_solutions(image):
    firstcols = [[[0], [0]], [[0], [1]], [[1], [0]], [[1], [1]]]
    firstrows = []
    for entry in firstcols:
        generate_first_row(entry, firstrows, image)
    # Now I use each potential first row I generated to generate full preimage matrices. The algorithm is mostly the
    # same, except I get to work with the sums of 3 neighbors instead of 2.
    for row in firstrows:
        # print(row)
        fill_preimages(row[1], image, 1)
    return 0


def grid_sum(grid):
    """
    To make code more readable.

    :param grid: A 2x2 grid to return the sum of.
    :return: The sum of a 2x2 grid.
    """
    return grid[0][0] + grid[0][1] + grid[1][0] + grid[1][1]


# @profile
def answer(g):
    # A simple brute-force approach first.
    global count
    count = 0
    g = bool_to_int(g)
    generate_solutions(g)
    return count

if __name__ == '__main__':
    import time

    start = time.time()
    case0 = [[True, False],
             [False, True]]
    print("\n\nCase 0: \n", case0[0], "\n", case0[1],
          "\n\nExpected: 12. Calculated: {}".format(answer(case0)))
    print("Time elapsed:", time.time() - start)

    start = time.time()
    case1 = [[True, False, True],
             [False, True, False],
             [True, False, True]]
    print("\n\nCase 1: \n", case1[0], "\n", case1[1], "\n", case1[2],
          "\n\nExpected: 4. Calculated: {}".format(answer(case1)))
    print("Time elapsed:", time.time() - start)

    start = time.time()
    case2 = [[True, False, True, False, False, True, True, True],
             [True, False, True, False, False, False, True, False],
             [True, True, True, False, False, False, True, False],
             [True, False, True, False, False, False, True, False],
             [True, False, True, False, False, True, True, True]]
    print("\n\nCase 2: \n", case2[0], "\n", case2[1], "\n", case2[2], "\n", case2[3],
          "\n\nExpected: 254. Calculated: {}".format(answer(case2)))
    print("Time elapsed:", time.time() - start)

    start = time.time()
    case3 = [[True, True, False, True, False, True, False, True, True, False],
             [True, True, False, False, False,False, True, True, True, False],
             [True, True, False, False, False, False, False, False, False, True],
             [False, True,False, False, False, False, True, True, False, False]]
    print("\n\nCase 3: \n", case3[0], "\n", case3[1], "\n", case3[2], "\n", case3[3],
          "\n\nExpected: 11567. Calculated: {}".format(answer(case3)))
    print("Time elapsed:", time.time() - start)

