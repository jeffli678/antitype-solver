import enchant
import sys
import itertools 

d = enchant.Dict("en_US")

def parse_input(user_input):
    
    user_input_split = user_input.split(' ')
    
    if len(user_input_split) == 2:
        up, down = user_input_split
    else:
        up, down, rounds = user_input_split

    up = up.strip().replace('0', ' ')
    down = down.strip().replace('0', ' ')
    if not len(up) == len(down):
        print('Warning: input length does not match!')
    
    try:
        rounds = int(rounds)
    except:
        rounds = 2

    return [up, down], rounds

def is_valid_pos(pos, val):
    if not pos[0] in (0, 1):
        return False
    
    s = val[pos[0]]
    return 0 <= pos[1] < len(s) and (not s[pos[1]] == ' ')

def replace_char(s, idx):
    old_char = s[idx]
    if not old_char == 'z':
        new_char = chr(ord(old_char) + 1)
    else:
        new_char = 'a'
    
    new_s = s[ : idx] + new_char + s[idx + 1 :  ]
    return new_s

def replace_at(val, pos):
    
    val[pos[0]] = replace_char(val[pos[0]], pos[1])

    return val

def eval_op(val, op):

    l = len(val[0])
    directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
    for direction in directions:
        new_pos = (op[0] + direction[0], op[1] + direction[1])
        if is_valid_pos(new_pos, val):
            val = replace_at(val, new_pos)

    return val

def eval_op_list(init, op_list):

    # make a copy of it
    val = init[:]
    for op in op_list:
        val = eval_op(val, op)

    val[0] = val[0].strip()
    val[1] = val[1].strip()

    return val

def check_solution_valid(result):
    # return True
    return d.check(result[0]) and d.check(result[1])

def solve(user_input, rounds):

    possible_moves = []
    
    for i in range(2):
        for j in range(len(user_input[0])):
            if not user_input[i][j] == ' ':
                possible_moves.append((i, j))

    op_lists = itertools.product(possible_moves, repeat = rounds)

    candidate_solutions = []
    candidate_moves = []

    for op_list in op_lists:

        result = eval_op_list(user_input, op_list)
        # print(op_list)
        # print(result)
        if check_solution_valid(result):
            candidate_solutions.append(tuple(result))
            candidate_moves.append(op_list)
        
    return candidate_solutions, candidate_moves

def print_move(move, l):
    
    move_str = []
    for i in range(2):
        move_str.append([])
        for _ in range(l):
            move_str[i].append('0')

    for info in move:
        line_idx = info[0]
        idx = info[1]
        move_str[line_idx][idx] = '*'

    s = ''.join(move_str[0]) + '\n' + ''.join(move_str[1])
    
    print(s)
    return s


def main():

    while True:

        solution_set = set()

        while True:

            tip = 'Please type the two words, followed by the number of steps allowed.\
                \nNote: use 0 to represent space and space to delimit the words and number.\
                \nIf the two words have different length, use proper leading and/or trailing 0 to compensante for it\
                \ne.g., for challenge 45, type: \
                \ngaoox 00rzc 3\
                \n'
            print(tip)

            user_input = raw_input('')
            user_input, rounds = parse_input(user_input)

            print('\nThe input is: ')
            print(user_input[0])
            print(user_input[1])

            if not rounds > 0:
                rounds = 2

            print('rounds: %d' % rounds)
            print('')

            candidates, moves = solve(user_input, rounds)

            if len(solution_set) == 0:
                solution_set = set(candidates)

            else:
                solution_set = solution_set.intersection(candidates) 

            solution_count = len(solution_set)

            if solution_count == 0:
                print('Unable to solve it. ')
                break

            if solution_count <= 5:

                solution_list = list(solution_set)
                for i in range(solution_count):

                    solution = solution_list[i]
                    print(solution)
                    idx = candidates.index(solution)
                    move = moves[idx]
                    print_move(move, len(user_input[0]))
                    print('')
                break
                
            else:
                print('there are still %d possibe solutions, please give more hints' \
                    % len(solution_set))
                print('How? Restart the same level and the game will give you two different hints for the same puzzle')
            

    


if __name__ == '__main__':
    main()


# gaoox 00rzc 3

# The input is: 
# gaoox
#   rzc
# rounds: 3

# ('happy', 'sad')
# 0*000
# 000**

# ('happy', 'rad')
# 0*00*
# 0000*
