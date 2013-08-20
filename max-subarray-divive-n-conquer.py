def FindMaxCrossing(A, low, mid, high):
    # Tim max subarray ben trai
    tong = 0
    tong_trai = tong + A[mid]
    chiso_trai = mid
    for i in range(mid,low-1,-1):
        tong += A[i]
        if tong > tong_trai:
            tong_trai = tong
            chiso_trai = i
    # Tim max subarray ben phai
    tong = 0
    tong_phai = tong + A[mid+1]
    chiso_phai = mid+1
    for j in range(mid+1, high+1):
        tong += A[j]
        if tong > tong_phai:
            tong_phai = tong
            chiso_phai = j
    return chiso_trai, chiso_phai, tong_trai + tong_phai

def FindMaxSubarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high)/2
        trai_low, trai_high, trai_sum = FindMaxSubarray(A, low, mid)
        phai_low, phai_high, phai_sum = FindMaxSubarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = FindMaxCrossing(A,low,mid,high)
        if trai_sum >= phai_sum and trai_sum >= cross_sum:
            return trai_low, trai_high, trai_sum
        elif phai_sum >= trai_sum and phai_sum >= cross_sum:
            return phai_low, phai_high, phai_sum
        else:
            return cross_low, cross_high, cross_sum

            
            
        
        
    
    
