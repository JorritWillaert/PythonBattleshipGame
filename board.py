from box import Box

class Board(Box):
    def __init__(self):
        """Initialize the board empty."""
        self.board = []
        self.hitted_not_sunk = [] #Only for CPU
        for row in range(10):
            line = []
            for column in range(10):
                element = Box('.', (row, column))
                line.append(element)
            self.board.append(line)

    def print_board(self, person):
        """Print out board."""
        print("    A B C D E F G H I J")
        index = 1
        for line in self.board:
            if index != 10:
                end = '   '
            else:
                end = '  '
            print(index, end = end)
            index += 1
            for element in line:
                if (element.symbol != '.' and element.is_visible == True) or person == 'own':
                    print(element.symbol, end = " ")
                else:
                    print(end = ". ")
            print('')
        print('')

    def find_coordinate(self, coordinate):
        """Find the box object corresponding with that coordinate."""
        for line in self.board:
            for element in line:
                if element.place == coordinate:
                    return element
