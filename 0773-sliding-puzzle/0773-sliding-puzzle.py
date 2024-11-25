class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        res = "123450"
        s = ''.join(str(num) for row in board for num in row)
        
        n = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        
        queue = deque([(s, 0)])  
        visited = set()
        visited.add(s)
        
        while queue:
            state, moves = queue.popleft()
            
            if state == res:
                return moves
            
            zero_index = state.index('0')
            
            for neighbor in n[zero_index]:
                new_state = list(state)
                new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]
                new_state_str = ''.join(new_state)
                
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves + 1))
        return -1