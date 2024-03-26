def reverse_list(arr: list) -> list:
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    return arr

# print(reverse_list([1,2,3]))

def reverse_lst(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    return arr

# print(reverse_list([1,2,3,4,5], 3, 4))
        
def reverse_part(arr: list, k) -> list:
    n = len(arr)

    reverse_lst(arr, 0, n-1)
    reverse_lst(arr, 0, k % n-1) #k mod n
    reverse_lst(arr, k % n, n-1) 
    return arr

# print(reverse_part([1,2,3,4,5], 2))

def merge_lists(arr1, arr2):
   merged_array = []
   i = 0
   j = 0
   while (i < len(arr1)) and (j < len(arr2)):
    if arr1[i] < arr2[j]:
        merged_array.append(arr1[i])
        i +=1
    else:
        merged_array.append(arr2[j])
        j +=1
    if len(arr1) < len(arr2):
        merged_array = merged_array + arr2[j:]
    else:
        merged_array = merged_array + arr1[i:]
        
    return merged_array

# print(merge_lists([1,3,5], [2,3,4,5]))


#  DOESN'T WORK 

# def merge_seminar(arr1, arr2):
#     pointer1 = len(arr1) - len(arr2) -1 
#     pointer2 = len(arr2) -1
#     pointer3 = len(arr1) -1
#     while pointer2 >=0:
#         if (pointer1 >=0) and (arr1[pointer1] > arr2[pointer2]):
#             arr1[pointer3] = arr1[pointer1]
#             pointer1 -=1
#         else:
#             arr1[pointer3] = arr2[pointer2]
#             pointer2 -=1
#         pointer3 -=1
#     return arr1

# print(merge_seminar([1,3,5], [2,3,4,5]))

def merge(arr1, arr2):
    res = []
    i, j = 0, 0
    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        elif i < len(arr1):
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    return res

# print(merge([1,3,5], [2,3,4,5]))

def odd_vs_honest(arr):
    evenindex = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[evenindex] = arr[evenindex], arr[i]
            evenindex +=1
    return arr

# print(odd_vs_honest([1,2,3,4,5,6,7]))



# HOME TASK
def nulls_in_end(arr)-> list:
    null = len(arr) - 1 
    for i in range(len(arr)-1 ,0, -1):
        if arr[i] == 0:
            arr[i], arr[null] = arr[null], arr[i]
            null -= 1
    return arr
    
# print(nulls_in_end([1,0,23,4,330,0,0,5]))



