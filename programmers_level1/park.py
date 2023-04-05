# def solution(park, routes):
#     answer = []
#
#     max_width = len(park[0])
#     max_height = len(park)
#
#     i = 0
#     j = 0
#
#     park = [list(p) for p in park]
#
#     for p_i in range(0, max_height - 1):
#         for p_j in range(0, max_width - 1):
#             if park[p_i][p_j] == 'S':
#                 i, j = p_i, p_j
#                 break
#
#     d_pm = {'E': 1, 'S': 1, 'W': -1, 'N': -1}
#
#     for r in routes:
#         direction, d_size = r.split()
#
#         if direction in ('E', 'W'):
#             t_j = j
#             d_j = j
#             for _ in range(1, int(d_size) + 1):
#                 t_j = t_j + d_pm[direction]
#
#                 if t_j >= max_width or t_j < 0:
#                     j = d_j
#                     break
#                 else:
#                     if park[i][t_j] == "X":
#                         j = d_j
#                         break
#                     j = t_j
#         if direction in ('S', 'N'):
#             t_i = i
#             d_i = i
#             for _ in range(1, int(d_size) + 1):
#                 t_i += d_pm[direction]
#                 if t_i >= max_height or t_j < 0:
#                     i = d_i
#                     break
#                 else:
#                     if park[t_i][j] == "X":
#                         i = d_i
#                         break
#                     i = t_i
#     return [i, j]


# def solution(park, routes):
#     answer = []
#
#     max_width_index = len(park[0]) - 1
#     max_height_index = len(park) - 1
#
#     i, j = 0, 0
#
#     for index, p in enumerate(park):
#         if p.find('S') > 0:
#             i, j = index, p.find('S')
#
#     op_pm = {'E': 1, 'S': 1, 'W': -1, 'N': -1}
#
#     check = 0
#     for index_test, r in enumerate(routes):
#         op, n = r.split(" ")
#         check = op_pm[op] * int(n)
#
#         if op in ['E', 'W']:
#             check += j
#
#             if check > max_width_index or check < 0:
#                 continue
#
#             min_x = park[i].find('X') if park[i].find('X') >= 0 else -1
#             max_x = park[i].rfind('X') if park[i].rfind('X') >= 0 else -1
#
#             if min_x > 0 and max_x > 0:
#                 if (min_x > j and min_x <= check) or (min_x < j and min_x >= check):
#                     continue
#                 if (max_x > j and max_x <= check) or (max_x < j and max_x >= check):
#                     continue
#
#             j = check
#
#         if op in ['S', 'N']:
#             check += i
#
#             if check > max_height_index or check < 0:
#                 continue
#
#             y_i = []
#             for i_i in range(0, max_height_index):
#                 if park[i_i][j] == 'X':
#                     y_i.append(i_i)
#
#             if y_i:
#                 max_y = max(y_i)
#                 min_y = min(y_i)
#             else:
#                 min_y, max_y = -1, -1
#
#             if min_y > 0 and max_y > 0:
#                 if (max_y < i and max_y >= check) or (max_y > i and max_y <= check):
#                     continue
#                 if (min_y < i and min_y <= check) or (min_y > i and max_y <= check):
#                     continue
#
#             i = check
#
#     return [i, j]


if __name__ == '__main__':
    solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])
    # solution(["OSO","OOO","OXO","OOO"]	, ["E 2","S 3","W 1"])
