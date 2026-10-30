def merge_sort(arr):
    # Base Case: Agar array mein 0 ya 1 element hai
    if len(arr) <= 1:
        return arr
    
    # Array ko beech se baanto
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # TODO: Dono halves ko recursively sort karwao
    # Hint: sorted_left = merge_sort(left_half)
    sorted_left = merge_sort(left_half) 
    sorted_right = merge_sort(right_half)

    # TODO: Dono sorted halves ko merge karke return karo
    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    
    # TODO: Jab tak dono lists mein elements hain, compare karo
    # Jo chhota ho, use result mein daalo, aur uska index badhao
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # TODO: Agar left mein elements bache hain toh result mein daalo
    while i < len(left):
        result.append(left[i])
        i += 1
    # TODO: Agar right mein elements bache hain toh result mein daalo
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Test karne ke liye:
print(merge_sort([64, 25, 12, 22, 11]))
print(merge_sort([]))
print(merge_sort([5]))
print(merge_sort([1, 2, 3, 4, 5]))
print(merge_sort([5, 4, 3, 2, 1]))