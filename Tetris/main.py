import random

class Grid:
    def __init__(self):
        # Initialize grid dimensions and create a 6x6 grid filled with spaces.
        self.ROW = 6
        self.COL = 6
        self.grid = [[' ' for _ in range(self.COL)] for _ in range(self.ROW)]
        self.block_char = '█'  # Character used to represent blocks in the grid.

    def display_box(self):
        # Print the grid bordered with lines to make it look like a box.
        print('┌' + '─' * (self.COL * 2 - 1) + '┐')
        for row in self.grid:
            print('│' + ' '.join(row) + '│')
        print('└' + '─' * (self.COL * 2 - 1) + '┘')

    def randomTypeOfBlock(self):
        # Generate a random block shape based on random dimensions between 1 and 3.
        BLOCK_HEIGHT = random.randint(1, 3)
        BLOCK_WIDTH = random.randint(1, 3)
        return [[self.block_char for _ in range(BLOCK_WIDTH)] for _ in range(BLOCK_HEIGHT)]

    def display_shape(self, shape):
        # Display the shape that is to be inserted into the grid.
        for row in shape:
            print(' '.join(row))

    def colToDrop(self, col, shape):
        # Determine if and where a shape can be dropped into the grid at the specified column.
        shape_height = len(shape)
        shape_width = len(shape[0])
        if col + shape_width > self.COL:
            return None  # Return None if the shape doesn't fit in the column.

        for start_row in range(self.ROW - shape_height, -1, -1):
            free = True
            for i in range(shape_height):
                for j in range(shape_width):
                    if self.grid[start_row + i][col + j] != ' ':
                        free = False
                        break
                if not free:
                    break
            if free:
                return start_row  # Return the row where the shape can be dropped.
        return None  # Return None if there's no space to drop the shape.

    def insertShape(self, col, shape):
        # Insert the shape into the grid at the specified column if possible.
        start_row = self.colToDrop(col, shape)
        if start_row is not None:
            for i in range(len(shape)):
                for j in range(len(shape[i])):
                    self.grid[start_row + i][col + j] = shape[i][j]
            print("Shape inserted at column", col, "starting row", start_row)

    def eliminateShape(self):
        # Check for any full rows of blocks and eliminate them.
        for i in range(len(self.grid)):
            if all(cell == self.grid[i][0] and cell != ' ' for cell in self.grid[i]):
                self.grid[i] = [' ' for _ in range(self.COL)]
                print(f"Row {i} eliminated")

def main():
    grid = Grid()
    while True:
        shape = grid.randomTypeOfBlock()
        grid.eliminateShape()
        grid.display_box()
        print("---------------------")
        print("Shape: ")
        grid.display_shape(shape)
        try:
            col = int(input("Enter a column (0 to 5): "))
            if col < 0 or col >= grid.COL:
                print("Column out of bounds, please enter a valid column between 0 and 5.")
                continue
            if grid.colToDrop(col, shape) is not None:
                grid.insertShape(col, shape)
            else:
                print("YOU LOSE")
                quit()
        except ValueError:
            print("Please enter a valid integer for the column.")

if __name__ == "__main__":
    main()
