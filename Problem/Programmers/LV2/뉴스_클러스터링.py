# https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3

def set_maker(s):
    ret = set()
    for i in range(1, len(s)):
        if (el := s[i-1:i+1].lower()).isalpha():
            num = 1
            while el + str(num) in ret:
                num += 1
            ret.add(el + str(num))
    return ret


def solution(str1, str2):
    set1 = set_maker(str1)
    set2 = set_maker(str2)
    result = len(set1 & set2) / len(set1 | set2) if len(set1 | set2) else 1
    return int(result * 65536)


if __name__ == '__main__':
    str1, str2, answer = 'FRANCE', 'french', 16384
    print(solution(str1, str2) == answer)
    str1, str2, answer = 'handshake', 'shake hands', 65536
    print(solution(str1, str2) == answer)
    str1, str2, answer = 'aa1+aa2', 'AAAA12', 43690
    print(solution(str1, str2) == answer)
    str1, str2, answer = 'E=M*C^2', 'e=m*c^2', 65536
    print(solution(str1, str2) == answer)