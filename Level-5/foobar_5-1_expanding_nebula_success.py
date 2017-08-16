# This mapping is the reverse of the mapping below: It maps 2x2 grids to states.
PREV_STATEMAP = {
    # For example, this pre-image grid maps to a state of 0:
    #   0 0
    #   0 0
    ((0, 0), (0, 0)): 0,
    # And this grid maps to 1.
    #   0 0
    #   0 1
    ((0, 0), (0, 1)): 1,
    ((0, 0), (1, 0)): 1,
    ((0, 0), (1, 1)): 0,
    ((0, 1), (0, 0)): 1,
    ((0, 1), (0, 1)): 0,
    ((0, 1), (1, 0)): 0,
    ((0, 1), (1, 1)): 0,
    ((1, 0), (0, 0)): 1,
    ((1, 0), (0, 1)): 0,
    ((1, 0), (1, 0)): 0,
    ((1, 0), (1, 1)): 0,
    ((1, 1), (0, 0)): 0,
    ((1, 1), (0, 1)): 0,
    ((1, 1), (1, 0)): 0,
    ((1, 1), (1, 1)): 0
}

# This mapping helps tie current states in the image to potential pre-image states.
CUR_STATEMAP = {
    # These are all 2x2 grids that will evaluate to 0 in the pre-image.
    0: (
        ((0, 0), (0, 0)),
        ((0, 0), (1, 1)),
        ((0, 1), (0, 1)),
        ((0, 1), (1, 0)),
        ((0, 1), (1, 1)),
        ((1, 0), (0, 1)),
        ((1, 0), (1, 0)),
        ((1, 0), (1, 1)),
        ((1, 1), (0, 0)),
        ((1, 1), (0, 1)),
        ((1, 1), (1, 0)),
        ((1, 1), (1, 1))
    ),
    # And these pre-image grids evaluate to 1.
    1: (
        ((1, 0), (0, 0)),
        ((0, 1), (0, 0)),
        ((0, 0), (1, 0)),
        ((0, 0), (0, 1))
    )
}


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


def generate_col(first, column):
    """
    Similar to my other algorithm for solving this question, we begin by determining
    all the possible configurations of the given column of pre-images.

    We do this by looking up the valid pre-image grids based on our first entry in the column, and then
    working from there trying the possibilities in botrows.

    :param first: Our first-level dictionary counting all of our occurrences of bottom rows.
    :param column: The right-most unanalyzed column (bottom-most row) of the MxN transposed matrix generated above.
    :return: All of the constructions of bottom rows possible given the preceding column in the matrix.
    """

    botrows = (
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    )

    possibilities = []

    # We iterate through our dictionary currently holding our sums of occurrences, because it contains all of our
    # valid bottom rows. If we don't have a valid pairing, there's nothing left to add. We return.
    for key in first:
        choices = []
        for row in botrows:
            # We try looking up the 2x2 grid composed here in our lookup table to see if it produces
            # the current state we're trying to append in our image matrix. We compose like so:
            #   [bottom row of previous],
            #   [choice in botrows     ]
            if PREV_STATEMAP[((key[0], key[1]), row)] == column[0]:
                # In the case of a match, we append the matching previous-state and bottom row combination.
                choices.append(row)

        for n in range(1, len(column)):
            next = []
            if choices is None:
                # This is where we return if nothing was previously constructed.
                return
            for col in choices:
                for m in range(2):
                    # We check if 0 or 1 complete our column choice's decision state.
                    temp = list(col)
                    if PREV_STATEMAP[((key[n], key[n + 1]), (col[n], m))] == column[n]:
                        # And if it does, we build that column, and append it to our next set of choices to iterate.
                        temp.append(m)
                        next.append(temp)
            # Now we operate on this set of columns, working our way down.
            choices = next

        # And here, we make sure to append every grid decision we make.
        [possibilities.append((key, tuple(choice))) for choice in choices]

    return tuple(possibilities)


def transpose(matrix):
    """
    Given our limitations on our NxM image matrix:
        1 <= N <= 9
        1 <= M <= 50
    It actually proves to improve our performance substantially to operate column-wise instead of row-wise.
    This is especially true because we limit the size of our column cache this way.

    :param matrix: An NxM matrix to transpose.
    :return: An MxN transposed matrix.
    """
    return tuple(zip(*matrix))


def generate_first_col(col):
    """
    Similar to my other algorithm for solving this question, we begin by determining
    all the possible configurations of the given column of pre-images.

    We do this by looking up the valid pre-image grids based on our first entry in the column, and then
    working from there trying the possibilities in botrows.

    :param col: The first row of the MxN transposed matrix generated above.
    :return: All of the constructions of first rows possible given the provided param. The solution is transposed
             to reflect that we're working on a transposed matrix.
    """

    botrows = (
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    )

    # First, we look up all the possible 2x2 grids that would lead into our current state at [0, 0].
    choices = CUR_STATEMAP[col[0]]
    for idx in range(1, len(col)):
        # Now we work our way across the column to construct the rows below our 2x2 grids, much like
        # we did in the less efficient recursive algorithm.
        columns = []
        for prev in choices:
            for botrow in botrows:
                # We try looking up the 2x2 grid composed here in our lookup table to see if it produces
                # the current state we're trying to append in our image matrix. We compose like so:
                #   [bottom row of previous],
                #   [choice in botrows     ]
                if PREV_STATEMAP[(prev[idx], botrow)] == col[idx]:
                    # In the case of a match, we append the matching previous-state and bottom row combination.
                    columns.append(prev[:]+(botrow,))
        # And we're storing our choices in tuples because tuples are much faster than lists.
        choices = tuple(columns)
    # And then we transpose the solutions because we transposed the original matrix.
    return tuple([transpose(sol) for sol in choices])


def answer(g):
    """
    We start by calculating the valid pre-images for each column, and then we transpose those solutions so we can work
    on them row-wise. We do this for every column, only counting states that overlap their bottom-most and upper-most
    rows.

    The number of occurrences of each bottom row, when calculated, are stored in a first-level dictionary with a counter
    for the number of occurrences.

    When we move on to the next level of the matrix, we store occurrences of logic branches in a
    second-level dictionary.

    The second-level dictionary becomes the first-level dictionary for each new cycle. We can add up the first-level
    dictionary's final count of occurrences when the calculations terminate, and get our number of valid states.

    :param g: An NxM matrix to calculate the number of possible pre-images for.
    :return: The number of possible pre-images for the provided image, g.
    """
    g = bool_to_int(g)
    rotation = transpose(g)
    # In this dictionary, we'll count all the occurrences of bottom-most rows in the pre-image. And then add that up
    # later to get our total number of valid pre-images.
    first = {}
    valid_preimages = generate_first_col(rotation[0])
    # And here is the first time we begin counting occurrences of bottom row solutions.
    for preimage in valid_preimages:
        if preimage[1] not in first:
            first[preimage[1]] = 1
        else:
            first[preimage[1]] = first[preimage[1]] + 1

    for n in range(1, len(rotation)):
        second = {}
        valid_preimages = generate_col(first, rotation[n])
        for preimage in valid_preimages:
            if preimage[0] in first:
                if preimage[1] in second:
                    # By definition, this valid bottom row occurs at least as many times as the row that precedes it.
                    second[preimage[1]] = first[preimage[0]] + second[preimage[1]]
                else:
                    second[preimage[1]] = first[preimage[0]]
            else:
                # If there's no overlap, there's no point in counting the solution. It's not a solution!
                pass
        first = second
    return sum(first.values())


if __name__ == '__main__':
    # These are all the test cases I used to validate the program.

    import time

    start = time.time()
    case0 = [
        [True, False],
        [False, True]
    ]
    print("\n\nCase 0: \n", case0[0], "\n", case0[1],
          "\n\n    Expected: 12\n  Calculated: {}".format(answer(case0)))
    print("Time elapsed:", time.time() - start)

    start = time.time()
    case1 = [
        [True, False, True],
        [False, True, False],
        [True, False, True]
    ]
    print("\n\nCase 1: \n", case1[0], "\n", case1[1], "\n", case1[2],
          "\n\n    Expected: 4\n  Calculated: {}".format(answer(case1)))
    print("Time elapsed:", time.time() - start)

    start = time.time()
    case2 = [
        [True, False, True, False, False, True, True, True],
        [True, False, True, False, False, False, True, False],
        [True, True, True, False, False, False, True, False],
        [True, False, True, False, False, False, True, False],
        [True, False, True, False, False, True, True, True]
    ]
    print("\n\nCase 2: \n", case2[0], "\n", case2[1], "\n", case2[2], "\n", case2[3], "\n", case2[4],
          "\n\n    Expected: 254\n  Calculated: {}".format(answer(case2)))
    print("Time elapsed:", time.time() - start)

    start = time.time()
    case3 = [
        [True, True, False, True, False, True, False, True, True, False],
        [True, True, False, False, False, False, True, True, True, False],
        [True, True, False, False, False, False, False, False, False, True],
        [False, True, False, False, False, False, True, True, False, False]
    ]
    print("\n\nCase 3: \n", case3[0], "\n", case3[1], "\n", case3[2], "\n", case3[3],
          "\n\n    Expected: 11567\n  Calculated: {}".format(answer(case3)))
    print("Time elapsed:", time.time() - start)

    start = time.time()
    case4 = [[False for n in range(50)] for n in range(9)]
    print("\n\nCase 4: \n", case4[0], "\n", case4[1], "\n", case4[2], "\n", case4[3], "\n",
          case4[4], "\n", case4[5], "\n", case4[6], "\n", case4[7], "\n", case4[8],
          "\n\n    Expected: 342015522530891220930318205106520120995761507496882358868830383880718255659276117597645436150624945088901216664965365050\
          \n  Calculated: {}".format(answer(case4)))
    print("Time elapsed:", time.time() - start)

    # This test was originally constructed as a stress-test for the caching implementation, since there are no
    # duplicate columns to use to optimize the large matrix.
    # However, it's still a decent test case.
    start = time.time()
    case5 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
         0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
         1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0,
         1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
         0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
    ]
    print("\n\nCase 5: \n", case5[0], "\n", case5[1], "\n", case5[2], "\n", case5[3], "\n",
          case5[4], "\n", case5[5], "\n", case5[6], "\n", case5[7], "\n", case5[8],
          "\n\n    Expected: 3242622241876453593959850247729073082350043061864\
          \n  Calculated: {}".format(answer(case5)))
    print("Time elapsed:", time.time() - start)
