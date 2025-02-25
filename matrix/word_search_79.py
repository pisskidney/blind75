from typing import List


class Solution:
    def go(self, visited, word, board, position) -> bool:

        if not word:
            return True

        if position[0] < 0 or position[0] >= len(board):
            return False

        if position[1] < 0 or position[1] >= len(board[0]):
            return False

        if board[position[0]][position[1]] != word[0]:
            return False

        if position in visited:
            return False

        visited.add(position)

        up = (position[0] - 1, position[1])
        down = (position[0] + 1, position[1])
        left = (position[0], position[1] - 1)
        right = (position[0], position[1] + 1)

        is_up = self.go(visited, word[1:], board, up)
        is_down = self.go(visited, word[1:], board, down)
        is_left = self.go(visited, word[1:], board, left)
        is_right = self.go(visited, word[1:], board, right)

        visited.remove(position)

        return is_up or is_down or is_left or is_right

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.go(set([]), word, board, (i, j)):
                    return True

        return False
