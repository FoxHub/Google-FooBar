# Foobar Level 2, Challenge 1.

def get_coord(num):
    """
    This will serve as a helper function in our algorithm.
    We're solving the knight's shortest path problem, so I'm
    breaking the input into a grid-like fashion.
    """
    x = int(num%8)
    y = int((num-x)/8)
    return x, y


def answer(src, dest):
    """
    I'll tackle this problem using recursion and depth-first search.

    :param src: The location we begin at.
    :param dest: The destination, an integer.
    :return: The shortest number of steps required to reach the destination.
    """
    class board:
        grid = grid = [[0 for col in range(8)] for row in range(8)]
    bunks = board()

    def dfs(srcx, srcy, level):
        """
        On each iteration of this algorithm, we will check all eight squares
        that our knight can reach from our source tile. If they have not
        yet been traversed to, we will mark them with our current
        recursion level, and then run this algorithm from those tiles.

        We use the created grid mapping to determine how many moves are required
        to reach dest from src.

        :param srcx: x co-ordinate of this recursive iteration
        :param srcy: y co-ordinate of this recursive iteration
        :param level: how many times we've called this function
        :return: nothing
        """
        def mark(x, y, level):
            if x not in range(8) or y not in range(8):
                return
            # A helper function mostly to keep our code readable.
            # We change the mark on the tile either if we find a larger level,
            if bunks.grid[x][y] > level or bunks.grid[x][y] == 0:
                bunks.grid[x][y] = level
                return True
        # This also isn't java, so we're not protected from out-of-bounds accesses.
        if srcx not in range(8) or srcy not in range(8):
            return
        # If the tile's level is not 0 and less than ours, our traversal to this point
        # is pointless. We return.
        if bunks.grid[srcx][srcy] != 0 and bunks.grid[srcx][srcy] < level-1:
            return
        # So first, the 8 possibilities.
        # We mark up...
        mark(srcx-1, srcy+2, level)
        mark(srcx+1, srcy+2, level)
        # Right...
        mark(srcx+2, srcy-1, level)
        mark(srcx+2, srcy+1, level)
        # Down...
        mark(srcx-1, srcy-2, level)
        mark(srcx+1, srcy-2, level)
        # Then left.
        mark(srcx-2, srcy-1, level)
        mark(srcx-2, srcy+1, level)
        # Then we traverse to these tiles and repeat the algorithm on each one.
        dfs(srcx-1, srcy+2, level+1)
        dfs(srcx+1, srcy+2, level+1)
        dfs(srcx+2, srcy-1, level+1)
        dfs(srcx+2, srcy+1, level+1)
        dfs(srcx-1, srcy-2, level+1)
        dfs(srcx+1, srcy-2, level+1)
        dfs(srcx-2, srcy-1, level+1)
        dfs(srcx-2, srcy+1, level+1)

    if src == dest:
        # If the coordinates are the same, we have no calculations to do.
        return 0
    else:
        srcx, srcy = get_coord(src)
        destx, desty = get_coord(dest)
        dfs(srcx, srcy, 1)
        print("End grid:")
        for num in range(8):
            print(bunks.grid[num])
        print("Moves to dest: " + str(bunks.grid[destx][desty]))
        return bunks.grid[destx][desty]