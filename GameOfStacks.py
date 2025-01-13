def twoStacks(maxSum, a, b):
    i, j, current_sum, count = 0, 0, 0, 0
    
    while i < len(a) and current_sum + a[i] <= maxSum:
        current_sum += a[i]
        i += 1
        count += 1
    
    max_count = count
    
    while j < len(b) and (i > 0 or current_sum + b[j] <= maxSum):
        current_sum += b[j]
        j += 1
        count += 1
        
        while current_sum > maxSum and i > 0:
            i -= 1
            current_sum -= a[i]
            count -= 1
        
        if current_sum <= maxSum:
            max_count = max(max_count, count)
    
    return max_count

g = int(input())
results = []

for _ in range(g):
    n, m, maxSum = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    results.append(twoStacks(maxSum, a, b))

for result in results:
    print(result)
