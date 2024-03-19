def matrix(n):
    if n % 2 == 0:
        raise ValueError("n must be odd")
    
    mat = [[0 for _ in range(n)] for _ in range(n)]
    
    x, y = n // 2, n // 2
    
    mat[x][y] = 1
    
    num = 2
    layer = 1
    
    while num <= n*n:
        for i in range(1, layer*2):
            if num > n*n: break
            y += 1
            mat[x][y] = num
            num += 1
        
        for i in range(1, layer*2):
            if num > n*n: break
            x -= 1
            mat[x][y] = num
            num += 1
        
        for i in range(1, layer*2 + 1):
            if num > n*n: break
            y -= 1
            mat[x][y] = num
            num += 1
        
        for i in range(1, layer*2 + 1):
            if num > n*n: break
            x += 1
            mat[x][y] = num
            num += 1
        
        layer += 1

    return mat


def average(matrix):
    n = len(matrix)
    
    sum_diag = sum(matrix[i][i] for i in range(n))
    
    avg_diag = sum_diag / n
    
    return avg_diag

print(average(matrix(4049)))




