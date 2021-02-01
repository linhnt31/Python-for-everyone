# Link: https://app.codesignal.com/tournaments/q34suwQKwaMczpqia/E

# Original 
# Time complexity: O(n) 
# Space complexity: O(n)
def reverseOnDiagonals(matrix):
    dis = len(matrix)
    a = []
    b = []
    for i in range(dis):
        a.append(matrix[i][i])
        b.append(matrix[i][dis-i-1])
        
    a.reverse()
    b.reverse()
    
    for i in range(dis):
        matrix[i][i] = a[i]
        matrix[i][dis-i-1] = b[i]
    
    return matrix