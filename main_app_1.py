# task 1

def ret_rev(line: str) -> str:
    line = line.split(" ")
    line = line[::-1]
    s = " ".join(line)

    return s

print(ret_rev("Hello my dear python"))

# task 2

def max_sum(nums: list):
    s = 0
    s_l = []
    for i in nums:
        s += i
        s_l.append(i)
        if s < 0:
            s = 0
            s_l = []

    return f"самый большой массив: {s_l}, его сумма: {s}"

# task 3

def char_frequency(line: str) -> dict:
    line_2 = set(line)
    line_3 = list(line_2)
    first_list = []

    for i in line_3:
        s = line.count(i)
        first_list.append(s)

    last_list = dict(zip(line_3, first_list))

    return last_list


# task 4

def are_anogr(w_1: str, w_2: str) -> str:
    w_1 = list(w_1)
    w_2 = list(w_2)
    w_1.sort()
    w_2.sort()

    return w_1 == w_2