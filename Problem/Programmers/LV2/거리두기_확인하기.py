# https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3

class Room:
    def __init__(self, place):
        self.place = place
    
    def _find_near_P(self, i, j):
        cnt = 0
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            I, J = i+di, j+dj
            if 0 <= I < 5 and 0 <= J < 5 and self.place[I][J] == 'P':
                cnt += 1
        return cnt
    
    def check(self):
        for i in range(5):
            for j in range(5):
                target = self.place[i][j]
                if target == 'P' and self._find_near_P(i, j):
                    return 0
                elif target == 'O' and self._find_near_P(i, j) >= 2:
                    return 0
        return 1
    

def solution(places):
    answer = []
    for place in places:
        answer.append(Room(place).check())
    return answer


if __name__ == '__main__':
    places, result = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                      ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                      ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                      ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                      ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]], [1, 0, 1, 1, 1]
    print(solution(places) == result)