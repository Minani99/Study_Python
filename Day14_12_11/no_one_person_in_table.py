can_sit = 2
max_can_sit = 100
max_person = 100
memo = {}


def problem(l, s):  # l>남은사람 s>앉힌사람
    key = str([l, s])

    if key in memo:
        return memo[key]
    if l < 0:
        return 0
    if l == 0:
        return 1

    count = 0
    for i in range(l, can_sit + 1):
        count += problem(l - i, i)
    memo[key] = count

    return count


print(problem(max_person, can_sit))
