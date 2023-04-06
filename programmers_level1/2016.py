from datetime import datetime


# 다른 사람의 답안
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]


def solution(a, b):
    answer = ''
    now = datetime(2016,a,b)
    answer = now.strftime("%a")
    return answer.upper()


if __name__ == '__main__':
    assert solution(5, 24) == "TUE"
