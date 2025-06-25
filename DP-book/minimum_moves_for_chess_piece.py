'''
Minimum Chess Moves Problem.
You have a special chess piece that can move like a Knight or a King.
A Knight moves in "L" shapes: 2 steps in one direction, then 1 step in the perpendicular direction.
A King moves 1 step in any direction (horizontal, vertical, or diagonal).
Given a starting cell and a target cell on a chessboard, find the minimum number of moves this piece needs to reach the target.
Write a function that takes the source and destination cell positions (like (x1, y1) and (x2, y2)) and returns the minimum number of moves required.
'''


def solve(src, dest):
    moves=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1),
           (1,2),(-1,2),(1,-2),(-1,-2),(1,-2)]
    dp={}
    def dfs(i , j):
        if i == dest[0]and j==dest[1]:
            return 0
        if (i,j)  in dp:
            return dp[(i,j)]
        dp[(i,j)]=1000
        for move in moves:
            if i+move[0]>= 0 and j+move[1]>= 0 and i+move[0]< 8 and j+move[1]< 8:
                dp[(i,j)]=min(dp[(i,j)],1+dfs(i+move[0],j+move[1]))
            else:
                continue
        return dp[(i,j)]
    return dfs(src[0],src[1])
if __name__ == '__main__':
    src=(0,0)
    dest=(1,2)
    print(solve(src, dest))