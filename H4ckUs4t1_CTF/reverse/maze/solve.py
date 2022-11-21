# g = KnightTourGraph[8, 8]
# path = FindHamiltonianPath[g, 36, 1]

path = [36, 53, 38, 55, 40, 30, 47, 64, 54, 37, 52, 35,
        50, 33, 27, 42, 57, 51, 41, 58, 43, 60, 45, 62, 56,
        39, 29, 23, 8, 14, 24, 7, 13, 19, 25, 10, 4, 21, 15,
        32, 22, 28, 34, 49, 59, 44, 61, 46, 63, 48, 31, 16,
        6, 12, 2, 17, 11, 5, 20, 26, 9, 3, 18, 1]

dir_map = [-2 * 8 + 1, -1 * 8 + 2, 1 * 8 + 2, 2 * 8 + 1, 2 * 8 - 1, 1 * 8 - 2, -1 * 8 - 2, -2 * 8 - 1]
# print(dir_map)

solution = ''
for i in range(len(path) - 1):
    start = path[i]
    end = path[i + 1]
    dir = dir_map.index(end - start) + 1
    solution += str(dir)

print(solution)

# 414174478585825527414142872163866612424766531414181767522568258

# $ ./maze _public
# Please type you input: 
# 414174478585825527414142872163866612424766531414181767522568258
# Well done! Please validate the input on the remote server
