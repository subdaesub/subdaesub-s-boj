from collections import Counter
import sys
input = sys.stdin.readline

def min_mex(arr, k):
    freq = Counter(arr)
    mex = 0

    while True:
        if freq[mex] <= k:
            return mex
        mex += 1
        
def max_mex(arr, k):
    arr_set = list(set(arr))
    cnt = 0
    
    if min(arr_set) > k:
        return k
    if max(arr_set) - len(arr_set) < k:
        return k + len(arr_set)
    while True:
        if k < arr_set[cnt] - cnt:
            return cnt + k
        cnt += 1

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(min_mex(arr, k))
print(max_mex(arr, k))