def bottom_up(n):  # Preferred | [1] -> [2] -> [3] -> ... -> [n]
    cache = (n+1)*[None]
    cache[1] = cache[2] = 1
    for i in range(3, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]


def top_down(n, cache=None):  # [n] -> [n-1] -> [n-2] -> ... -> [1]
    if cache is None:
        cache = (n+1) * [None]
    if n <= 2:
        cache[n] = 1
    elif cache[n] is None:
        cache[n] = top_down(n-1, cache) + top_down(n-2, cache)
    return cache[n]


# cache[n] 대신 n이 정답인 경우도 있다.
