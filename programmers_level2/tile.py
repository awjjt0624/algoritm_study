def solution(brown, yellow):
    answer = []

    tile_sum = brown + yellow

    yellow_width = 0
    yellow_height = 0
    brown_width = 0
    brown_height = 0

    for index in range(1, yellow+1):
        yellow_width = yellow // index

        if yellow % index > 0:
            continue

        brown_width = yellow_width + 2

        if tile_sum % brown_width > 0 or brown_width > brown:
            continue

        brown_height = tile_sum // brown_width
        break

    answer = [brown_width, brown_height]

    return answer


if __name__ == '__main__':
    # print(solution(24, 24))
    print(solution(8, 1))