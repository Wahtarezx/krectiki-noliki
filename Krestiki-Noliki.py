class Board:
    """Тестовая документация для класса Board"""
    def __init__(self):
        self.cell1 = Cell(11, 'n', 11, '')
        self.cell2 = Cell(12, 'n', 12, '')
        self.cell3 = Cell(13, 'n', 13, '')
        self.cell4 = Cell(21, 'n', 21, '')
        self.cell5 = Cell(22, 'n', 22, '')
        self.cell6 = Cell(23, 'n', 23, '')
        self.cell7 = Cell(31, 'n', 31, '')
        self.cell8 = Cell(32, 'n', 32, '')
        self.cell9 = Cell(33, 'n', 33, '')
        self.cells_list = [self.cell1, self.cell2, self.cell3,
                           self.cell4, self.cell5, self.cell6,
                           self.cell7, self.cell8, self.cell9]

        self.board = ['', '', '', '', '', '', '', '', '']

    def change_the_cell(self, number, symb):
        for i_cell in self.cells_list:
            if i_cell.busy == 'n' and i_cell.number == number:
                i_cell.busy = 'y'
                i_cell.symb = symb
                return True
        return False


    def end_the_game(self):
        self.win_mapping = {
            '1': self.cells_list[0].symb == self.cells_list[1].symb and self.cells_list[0].symb == self.cells_list[2].symb\
                    and self.cells_list[0].busy == 'y',
            '2': self.cells_list[3].symb == self.cells_list[4].symb == self.cells_list[5].symb\
                and self.cells_list[3].busy == 'y',
            '3': self.cells_list[6].symb == self.cells_list[7].symb == self.cells_list[8].symb\
                and self.cells_list[6].busy == 'y',
            '4': self.cells_list[0].symb == self.cells_list[3].symb == self.cells_list[6].symb\
                and self.cells_list[0].busy == 'y',
            '5': self.cells_list[1].symb == self.cells_list[4].symb == self.cells_list[7].symb\
                and self.cells_list[1].busy == 'y',
            '6': self.cells_list[1].symb == self.cells_list[4].symb == self.cells_list[7].symb\
                and self.cells_list[1].busy == 'y',
            '7': self.cells_list[2].symb == self.cells_list[5].symb == self.cells_list[8].symb\
                and self.cells_list[2].busy == 'y',
            '8': self.cells_list[0].symb == self.cells_list[4].symb == self.cells_list[8].symb\
                and self.cells_list[0].busy == 'y',
            '9': self.cells_list[2].symb == self.cells_list[4].symb == self.cells_list[6].symb\
                and self.cells_list[2].busy == 'y'
        }

        for win in self.win_mapping.values():
            if win:
                return True
        return False


class Cell:

    def __init__(self, value, busy, number, symb):
        self.value = value
        self.busy = busy
        self.number = number
        self.symb = symb


class Player:

    def __init__(self, name, wins_cnt=0):
        self.name = name
        self.wins_cnt = wins_cnt

    def move(self):
        while True:
            cell = int(input('Введите ваш ход: '))
            if cell in [11, 12, 13,
                        21, 22, 23,
                        31, 32, 33]:
                return cell

            print('Неверное значение клетки, попробуйте еще раз')


class Game:

    def __init__(self, status, player1, player2, board):
        self.status = status
        self.players = [player1, player2]
        self.board = board

    def start_of_the_move(self, player, symb):
        move = player.move()
        board.change_the_cell(move, symb)
        end = board.end_the_game()
        return end

    def start_one_game(self):
        board.cell1 = Cell(11, 'n', 11, '')
        board.cell2 = Cell(12, 'n', 12, '')
        board.cell3 = Cell(13, 'n', 13, '')
        board.cell4 = Cell(21, 'n', 21, '')
        board.cell5 = Cell(22, 'n', 22, '')
        board.cell6 = Cell(23, 'n', 23, '')
        board.cell7 = Cell(31, 'n', 31, '')
        board.cell8 = Cell(32, 'n', 32, '')
        board.cell9 = Cell(33, 'n', 33, '')
        board.cells_list = [board.cell1, board.cell2, board.cell3,
                           board.cell4, board.cell5, board.cell6,
                           board.cell7, board.cell8, board.cell9]

        for checker in range(10):
            if checker % 2 == 0:
                print('\nЛеха ходит')
                if self.start_of_the_move(player1, 'X'):
                    print('Леха выиграл\n')
                    player1.wins_cnt += 1
                    break
            else:
                print('\nНастюха ходит')
                if self.start_of_the_move(player2, 'O'):
                    print('Настена победила\n')
                    player2.wins_cnt += 1
                    break
            print('Ничья')

    def start_the_game(self):
        while True:
            print(f'{player1.name} выиграл {player1.wins_cnt} раз\n{player2.name} выиграл {player2.wins_cnt} раз')
            self.start_one_game()
            continue_the_game = input('Желаете продолжить игру? Y/N: ').lower()
            if continue_the_game == 'n':
                return print('Досвидания! Ждем вас снова')

            print('Погнали!')


board = Board()
player1 = Player('Алексей')
player2 = Player('Настена')
game = Game('+', player1, player2, board)
game.start_the_game()






