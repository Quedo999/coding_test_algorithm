"""
패배조건
    - 자신의 차례에 캐릭터가 움직일 수 없는 경우
    - 두 캐릭터가 같은 곳에 위치해있을때 상대 캐릭터가 이동할 경우
"""

def solution(board, aloc, bloc):
    answer = -1

    dy = [1, -1, 0 , 0]
    dx = [0 ,0, 1, -1]
    def dfs():
        return

    return answer

board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]
print(solution(board, aloc, bloc))