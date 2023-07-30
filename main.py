import math

def get_size(list_of_values):
    return round(math.sqrt(len(list_of_values)))

def get_tile_list(tiles):
    return tiles.split(',')

def draw_row(data_list):
    row_string = '│'
    for label in data_list:
        if len(label) == 0:
            row_string += '    │'
        elif len(label) == 1:
            row_string += '  ' + label + ' │'
        elif len(label) == 2:
            row_string += ' ' + label + ' │'
            
    return row_string

def draw_grid(grid_size, tile_list):
    last_row_index = len(tile_list) - grid_size
    
    print('┌────' + (('┬────') * (grid_size - 1)) + '┐')

    for i in range(0, len(tile_list), grid_size):
        print(draw_row(tile_list[i: i + grid_size]))
        
        if i != last_row_index:
            print('├────' + (('┼────') * (grid_size - 1)) + '┤')
        
    print('└────' + (('┴────') * (grid_size - 1)) + '┘')

def is_vertically_adjacent(grid_size, first_index, second_index):
    return abs(first_index - second_index) == grid_size

def is_horizontally_adjacent(grid_size, first_index, second_index):
    return first_index // grid_size == second_index // grid_size and abs(first_index - second_index) == 1

def get_valid_moves(grid_size, tile_list):
    blank_space_index = tile_list.index("")
    valid_moves = []
    
    for i in range(len(tile_list)):
        if (is_vertically_adjacent(grid_size, i, blank_space_index) or is_horizontally_adjacent(grid_size, i, blank_space_index)):
           valid_moves.append(tile_list[i])

    return valid_moves

def get_move(valid_moves):
    while True:
        move = input("Your move: ")
        if move in valid_moves or move == "quit":
            return move
        else:
            print(f"{move} is not valid. Try again.")

def swap_tile(tile_list, move):
    blank_space_index = tile_list.index("")
    move_index = tile_list.index(move)

    tile_list[blank_space_index] = tile_list[move_index]
    tile_list[move_index] = ""

def is_complete(tile_list):
    numbers_only_list = []
    for tile in tile_list:
        if tile != "":
            numbers_only_list.append(int(tile))

    return numbers_only_list == sorted(numbers_only_list) and tile_list[-1] == ""

def main(tiles):
    tile_list = get_tile_list(tiles)
    grid_size = get_size(tile_list)
    
    draw_grid(grid_size, tile_list)
              
    number_of_moves = 0
    while not is_complete(tile_list):
        move = get_move(get_valid_moves(grid_size, tile_list))
        if move == "quit":
            print("Goodbye!")
            return
        
        swap_tile(tile_list, move)
        draw_grid(grid_size, tile_list)
        number_of_moves += 1

    print(f"You won in {number_of_moves} moves. Congratulations!")
