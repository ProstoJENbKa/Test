import sys

def circular_path(n, m):
    arr = list(range(1, n + 1))
    idx = 0          
    path = []         

    while True:
        path.append(arr[idx])

        for step in range(m - 1):
            idx += 1
            if idx == n:   
                idx = 0   

        if idx == 0:
            break

    return ''.join(str(x) for x in path)

if len(sys.argv) != 3:
    print("Ошибка! Запустите так: python task1.py n m")
else:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print(circular_path(n, m))