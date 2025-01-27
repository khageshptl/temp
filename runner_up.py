if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    m = max(arr)
    
    c = arr.count(m)
    
    for i in range(c):
        arr.remove(m)
    
    print(max(arr))