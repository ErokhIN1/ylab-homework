""" Task 1"""


def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


""" Task 2 """


# Variant with standard library 'ipadress'
def int32_to_ip(int32: int) -> str:
    import ipaddress
    return str(ipaddress.ip_address(int32))


# Custom variant
def int32_to_ip_v2(int32: int) -> str:
    result = ''
    for i in [3, 2, 1, 0]:
        temp = str(int32 / (256 ** i))
        result += temp.split('.')[0] + '.'
        int32 = int32 % (256 ** i)
    return result.rstrip('.')


""" Task 3"""


def zeros(n: int) -> int:
    result = 0
    while n > 0:
        n //= 5
        result += n
    return int(result)


""" Task 4 """


def bananas(s: str) -> set:
    from itertools import combinations
    result = set()

    for i in combinations(range(len(s)), len(s) - 6):
        arr = list(s)
        for y in i:
            arr[y] = '-'
        arr = ''.join(arr)
        if arr.replace('-', '') == 'banana':
            result.add(arr)
    return result


""" Task 5 """


def count_find_num(primesL: list, limit: int) -> []:
    from functools import reduce
    first_num = reduce(lambda a, b: a * b, primesL, 1)
    if first_num > limit:
        return []
    nums = [first_num]
    for i in primesL:
        for n in nums:
            num = n * i
            while (num <= limit) and (num not in nums):
                nums.append(num)
                num *= i

    return [len(nums), max(nums)]
