
##1

def prob1(points):
    points = sorted(points, key=lambda x:x[1], reverse=True)
    max_x = -1
    for item in points:
        if item[0]>max_x:
            print(item)
            max_x = item[0]
if __name__ == "__main__":
    points = [[1,2],[5,3],[4,6],[7,5],[9,0]]
    prob1(points)