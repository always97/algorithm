def rotate_90(grid):
    N = len(grid)
    return [[grid[N - j - 1][i] for j in range(N)] for i in range(N)]

def is_sorted(grid):
    N = len(grid)
    # 행 체크
    for row in grid:
        if any(row[i] > row[i + 1] for i in range(N - 1)):
            return False
    # 열 체크
    for col in range(N):
        for row in range(N - 1):
            if grid[row][col] > grid[row + 1][col]:
                return False
    return True

def find_original_grid(grid):
    for _ in range(4):
        if is_sorted(grid):
            return grid
        grid = rotate_90(grid)
    return None

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

original_grid = find_original_grid(grid)

for row in original_grid:
  print(' '.join(map(str, row)))