# Foobar Level 3, Challenge 1, Attempt 2.

# Since the Depth-first solution was not fast enough for Google's standards, we're going to try
# a Breadth-first solution. This solution is less memory-efficient, but much faster in terms of run time.
# This solution is, notably, extensible to other occurrences of this problem where we could
# bypass more walls.

from collections import deque


class Node:
    def __init__(self, x, y, bypasses, grid):
        """
        :param x: The x coordinate of the node on our grid.
        :param y: The y coordinate of the node on our grid.
        :param bypasses: The number of walls we can skip.
        :param grid: The grid itself. All nodes know of the original matrix.
        """
        self.x = x
        self.y = y
        self.bypasses = bypasses
        self.grid = grid

    def __eq__(self, comp):
        """
        Overloading the equals operator
        :param comp: A node to compare to.
        :return: Whether or not the two nodes have identical contents. True or False.
        """
        return self.x == comp.x and self.y == comp.y and self.bypasses == comp.bypasses

    def __hash__(self):
        """
        This will uniquely identify each node based on its coordinate
        by numbering nodes left to right, top to bottom.

        This hash function allows us to store nodes in our queue in our solution.

        :return: A unique identifier for this node.
        """
        return self.x + len(self.grid) * self.y

    def get_vertices(self):
        """
        This function returns all the possible paths from our node.

        When we initialize each vertex, we keep track of if we've passed
        a wall up to this point. We don't treat any walls as vertices if we have.

        :return: A list of nodes that are passable from this node. May return an empty set.
        """
        vertices = []
        x = self.x
        y = self.y
        bypasses = self.bypasses
        grid = self.grid
        width = len(grid[0])
        height = len(grid)

        # It's important that we make sure we're not the left wall of the maze, or else
        # we'd be appending vertices out of our maze.
        if x > 0:
            wall = grid[y][x - 1] == 1
            if wall:
                if bypasses > 0:
                    # We decrement the number of walls we can pass from this point on in
                    # the traversal graph. Once this value reaches 0, we will no longer
                    # treat walls as passable.
                    vertices.append(Node(x - 1, y, bypasses - 1, grid))
                else:
                    # In this case, we do nothing. We can't possibly travel
                    # to this neighbor, so we don't add it to the list of vertices.
                    pass
            else:
                # No special logic is required if the node is not a wall.
                vertices.append(Node(x - 1, y, bypasses, grid))

        # Similarly, we want to avoid going out of bounds to the right, and so on.
        if x < width - 1:
            # The logic for the following portion in each case is identical to the first.
            wall = grid[y][x + 1] == 1
            if wall:
                if bypasses > 0:
                    vertices.append(Node(x + 1, y, bypasses - 1, grid))
                else:
                    pass
            else:
                vertices.append(Node(x + 1, y, bypasses, grid))

        if y > 0:
            wall = grid[y - 1][x] == 1
            if wall:
                if bypasses > 0:
                    vertices.append(Node(x, y - 1, bypasses - 1, grid))
                else:
                    pass
            else:
                vertices.append(Node(x, y - 1, bypasses, grid))

        if y < height - 1:
            wall = grid[y + 1][x]
            if wall:
                if bypasses > 0:
                    vertices.append(Node(x, y + 1, bypasses - 1, grid))
                else:
                    pass
            else:
                vertices.append(Node(x, y + 1, bypasses, grid))

        # This list should include all of our adjacent passable nodes.
        # It may be empty!
        return vertices


class PathFinder:
    def __init__(self, grid, bypasses):
        """
        :param grid: The matrix resembling our maze.
        :param bypasses: The number of walls that we can pass on this iteration of the algorithm.
        """
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.bypasses = bypasses

    def shortest_path(self):
        """
        We employ breadth-first search to find the shortest path to the exit of the maze.
        To do this, we add each node to a queue if it hasn't been visited yet, while tracking
        the distance that's been traveled by our current node.

        :return: An integer describing the length of the shortest path to the maze's bottom-right
                 square (its exit).
        """
        source = Node(0, 0, self.bypasses, self.grid)
        queue = deque([source])
        distance_map = {source: 1}

        while queue:
            # Grab the left-most element (the 'head' of our queue).
            curr = queue.popleft()

            # We're at the exit. This is our solution.
            if curr.x == self.width - 1 and curr.y == self.height - 1:
                return distance_map[curr]

            # If we're not at the end of the maze, then it's time to append its neighbours
            # to our queue so they'll be traversed later.
            for neighbor in curr.get_vertices():
                # This is where that hash function comes into play.
                if neighbor not in distance_map.keys():
                    distance_map[neighbor] = distance_map[curr] + 1
                    queue.append(neighbor)


def answer(maze):
    router = PathFinder(maze, 1)
    return router.shortest_path()


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
