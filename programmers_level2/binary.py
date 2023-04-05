

def count_val(s, zero_count: int = 0, bin_count: int = 0):
    val = ""
    result = []
    if len(s) == 1:
        return [bin_count, zero_count]

    else:
        for s_s in s:
            if s_s == "1":
                val += s_s
            else:
                zero_count += 1
        aa = len(val)
        tt = bin(aa)
        bin_count += 1
        return count_val(tt[2:], zero_count=zero_count, bin_count=bin_count)


def solution(s):
    answer = count_val(s)

    return answer


if __name__ == '__main__':
    s = "110010101001"
    answer = solution(s)
    print(answer)
