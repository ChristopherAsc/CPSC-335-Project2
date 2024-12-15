"""
The Red Team starts at row 0 and column 0 (0,0) at the top-left corner. Each period
represents a passable spot and each X represents an opponent-occupied spot (i.e. an impenetrable
spot). The Red Team's goal is to plan a passable route to cross the field, and reach the opponents'
goal post at (r-1,c-1), while avoiding the occupied cells. The problem objective is to compute the
number of different paths to cross the field. Two paths are different if they differ by at least one location.

In this algorithm, I will use a dynamic programming (DP) approach:
    - I will create a DP matrix A, where A[i][j] represents the number of distinct valid paths
      from (0,0) to (i,j).
    - The recurrence relation is:
        A[i][j] = A[i-1][j] + A[i][j-1]
      provided that the cell is passable ('.'). If the cell is blocked ('X'), then A[i][j] = 0.
    - The base case is A[0][0] = 1 if the start is passable.

    Arguments:
        grid (List[str]): The playing field where:
            '.' = valid move location
            'X' = opponent position (blocked cell)
    Returns:
        int: Number of valid paths from (0,0) to (r-1,c-1)
"""

# Grid from the problem (same as in Algo 1 for consistency)
grid = [
    "......X.X",
    "X........",
    "...X...X.",
    "..X....X.",
    ".X....X..",
    "....X....",
    "..X.....X",
    "........."
]

def soccer_dyn_prog(grid):
    # Number of rows and columns
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # If grid is empty or invalid, return 0
    if rows == 0 or cols == 0:
        return 0

    # Check if start or end position is blocked
    if grid[0][0] == 'X' or grid[rows-1][cols-1] == 'X':
        return 0

    # Initialize the DP matrix with zeros
    A = [[0]*cols for _ in range(rows)]

    # Base case: start position is always reachable in exactly one way if not blocked
    A[0][0] = 1

    # Fill the DP table
    for i in range(rows):
        for j in range(cols):
            # If this is the start cell, it's already set to 1 above
            if i == 0 and j == 0:
                continue

            # If cell is blocked, no paths go here
            if grid[i][j] == 'X':
                A[i][j] = 0
                continue

            # Count paths from top
            above = A[i-1][j] if i > 0 and grid[i-1][j] == '.' else 0
            # Count paths from left
            left = A[i][j-1] if j > 0 and grid[i][j-1] == '.' else 0

            # Total paths to (i,j)
            A[i][j] = above + left

    # The bottom-right corner holds the number of valid paths to reach the goal
    return A[rows-1][cols-1]

# Calculate and print result
result = soccer_dyn_prog(grid)
print(f"Number of valid paths (DP): {result}")  # Expected output: 102
