# Foobar Level 3, Challenge 1, Attempt 1.

def answer(maze):
    """
    I can largely re-use my code from foobar2-1.

    We'll traverse the maze like a graph. I debated converting it to one, but
    determined it won't do much to make the algorithm more intuitive.

    To solve this question, I perform a depth-first search and then look up the distance to the exit.

    :param maze: The maze to solve.
    :return: The distance to the southeastern corner of the maze.
    """

    class grid:
        grid = []
        width = len(maze)
        height = len(maze[0])
        costs = []
    ourmaze = grid()
    ourmaze.grid = maze
    ourmaze.costs = [[10000 for col in range(ourmaze.width)] for row in range(ourmaze.height)]

    def dfs(x, y, currcost, passedwall):
        """
        On each pass of this algorithm, we consider moving in every
        cardinal direction. If we've passed a wall already, we no
        longer try to pass any more.

        :param x: x co-ordinate of this recursive iteration
        :param y: y co-ordinate of this recursive iteration
        :param currcost: The current cost of our maze
        :return: nothing
        """

        # This isn't java, so we're not protected from out-of-bounds accesses.
        if x not in range(ourmaze.width) or y not in range(ourmaze.height):
            return
        # If a cost has been found that is lower than ours, this work is pointless.
        if currcost > ourmaze.costs[ourmaze.width-1][ourmaze.height-1]:
            return
        # As well, if we've already reach this node with a less expensive path, we exit.
        # But if we haven't, we update the cost.
        if currcost > ourmaze.costs[x][y]:
            return
        elif currcost < ourmaze.costs[x][y]:
            ourmaze.costs[x][y] = currcost
        # If we're on a 1, we have to do one of two things:
        if ourmaze.grid[x][y] == 1:
            # either exit
            if passedwall:
                return
            # or update passedwall
            else:
                passedwall = True
        dfs(x, y+1, currcost+1, passedwall)
        dfs(x+1, y, currcost+1, passedwall)
        dfs(x, y-1, currcost+1, passedwall)
        dfs(x-1, y, currcost+1, passedwall)

    dfs(0, 0, 1, False)
    return ourmaze.costs[ourmaze.width-1][ourmaze.height-1]


if __name__ == "__main__":

    case0 = [[0, 1, 1, 0],
             [0, 0, 0, 1],
             [1, 1, 0, 0],
             [1, 1, 1, 0]]
    print("\nCase 0:")
    for row in case0:
        print('', row)
    print("\n  Expected: 7\nCalculated: " + str(answer(case0)))

    case1 = [[0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 1],
             [0, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 0]]
    print("\nCase 1:")
    for row in case1:
        print('', row)
    print("\n  Expected: 11\nCalculated: " + str(answer(case1)))
