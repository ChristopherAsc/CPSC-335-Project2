"""
The Red Team starts at row 0 and column 0, i.e. coordinate (0,0) at the top-left corner. Each period
represents a passable spot and each X represents an opponent-occupied spot (i.e. an impenetrable
spot). The Red Team's goal is to plan a passable route to cross the field, and reach the opponents
goal post, while avoiding the occupied cells. The problem objective is to compute the number
of different paths to cross the field. Two paths are different if they differ by at least one location.
    
In this algorithm I will use bits to represent the algorithm, 1 = move right and 0 = move down
    Arguments:
        grid (List[List[str]]): The playing field where:
            '.' = valid move locations
            'X' = opponent positions
    Returns:
        int: Number of valid paths from (0,0) to (r-1,c-1)
"""

# Grid from the problem
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

def soccer_exhaustive(grid):
    # grid length and width
    rows = len(grid)
    cols = len(grid[0])

    # Check if start position (0,0) or end position (rows-1,cols-1) is blocked by opponent
    if grid[0][0] == 'X' or grid[rows-1][cols-1] == 'X':
        return 0
    if not grid or not grid[0]:     #Check if grid is valid
        return 0
    
    # Total moves needed to reach the goal
    path_length = rows + cols - 2
    
    #Check if bit sequence is a valid path, returns true if valid
    def is_valid_path(bits):

        # Start from top left corner
        row = col = 0
        
        # Process each bit, move right and move down operation
        for n in range(path_length):
            bit = (bits >> n) & 1
            
            if bit == 1:
                col += 1
            else:
                row += 1
                
            # Check if path goes outside grid boundaries
            if row >= rows or col >= cols:
                return False
                
            # Check if current position has an opponent
            if grid[row][col] == 'X':
                return False
                
        # For path to be valid it has to reach bottom right corner
        return row == rows-1 and col == cols-1
    
    counter = 0
    
    # Calculate all possible combinations (2^path_length)
    max_bits = 1 << path_length
    
    # Try all possible combinations of moves
    for bits in range(max_bits):
        right_moves = bin(bits).count('1')
        
        # Skip paths wihtout cols-1 right moves
        if right_moves != cols-1:
            continue

        if is_valid_path(bits):
            counter += 1
            
    return counter

# Calculate and print result
result = soccer_exhaustive(grid)
print(f"Number of valid paths: {result}")  # Expected output: 102