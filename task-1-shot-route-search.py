import itertools


def calculate_distance(point_1: tuple, point_2: tuple) -> float:
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def shot_route(dots: list[tuple]) -> str:
    start = dots.pop(0)
    points = list(itertools.permutations(dots, len(dots)))
    min_len_of_route = float('inf')
    res = None
    for p in points:
        len_of_route = 0
        last_element = start
        out_p = {}
        for i in p:
            points_len = calculate_distance(last_element, i)
            out_p[i] = points_len
            len_of_route += points_len
            last_element = i

        points_len = calculate_distance(last_element, start)
        out_p[f'{start}'] = points_len
        len_of_route += points_len
        if len_of_route < min_len_of_route:
            min_len_of_route = len_of_route
            res = out_p
    s = 0
    r = f'{start}'
    for k, v in res.items():
        s += v
        r += f' -> {k} distance: {v}'
    r += f' = {min_len_of_route}'
    return r


def main():
    points = [(0, 2),
              (2, 5),
              (5, 2),
              (6, 6),
              (8, 3)]
    print(shot_route(points))


if __name__ == "__main__":
    main()
