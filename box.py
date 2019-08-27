from colorama import Fore, Style
class Box():
    def __init__(self, symbol, place):
        self.hit = False
        self.symbol = symbol
        self.place = place
        self.is_visible = False

    def change_to_ship(self):
        """Change box from '.' to '@'."""
        self.symbol = '@'

    def change_to_sunk(self):
        self.symbol = Fore.RED + 'X' + Style.RESET_ALL
