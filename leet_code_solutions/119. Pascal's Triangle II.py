
from typing import List

def getRow(rowIndex: int) -> List[int]:
    last_row = []
    for row in range(rowIndex+1):
        row_data = [0 for _ in range(row+1)]
        row_data[0], row_data[-1] = 1,1
        for j in range(1, len(row_data)-1):
            row_data[j] = last_row[j-1]+last_row[j]
        last_row = row_data
    return last_row