# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

class ZipProgram:
    def __init__(self, s):
        self.s = s
        self.size = len(s)
    
    def zip_n(self, n):
        zip_size = self.size
        idx = n
        old_char = self.s[:idx]
        cnt = 1
        while idx+n <= self.size:
            char = self.s[idx:idx+n]
            if char == old_char:
                zip_size -= n
                cnt += 1
            elif cnt > 1:
                zip_size += len(str(cnt))
                cnt = 1
            idx += n
            old_char = char
        if cnt > 1:
            zip_size += len(str(cnt))
        return zip_size

        
def solution(s):
    zip_program = ZipProgram(s)
    min_size = zip_program.size
    for n in range(1, zip_program.size//2 + 1):
        if (zip_size := zip_program.zip_n(n)) < min_size:
            min_size = zip_size
    return min_size


if __name__ == '__main__':
    s, result = "aabbaccc", 7
    print(solution(s) == result)
    s, result = "ababcdcdababcdcd", 9
    print(solution(s) == result)
    s, result = "abcabcdede", 8
    print(solution(s) == result)
    s, result = "abcabcabcabcdededededede", 14
    print(solution(s) == result)
    s, result = "xababcdcdababcdcd", 17
    print(solution(s) == result)