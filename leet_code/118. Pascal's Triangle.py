
from typing import List

 def generate(numRows: int) -> List[List[int]]:
    triangle = []
    for row in range(numRows):
        row_data = [0 for _ in range(row+1)]
        row_data[0], row_data[-1] = 1,1
        for j in range(1, len(row_data)-1):
            row_data[j] = triangle[row-1][j-1]+triangle[row-1][j]
        triangle.append(row_data)
    return triangle


