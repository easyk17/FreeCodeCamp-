def quick_sort(arr):
    # Base Case: 0 ya 1 element
    if len(arr) <= 1:
        return arr
    
    # TODO: Pivot chuno (last element)
    pivot = arr[-1]
    
    # TODO: Left aur Right lists banao
    left = []
    right = []
    
    # TODO: Loop chalao arr ke saare elements par (except last)
    # Jo pivot se chhote, left mein daalo
    # Jo pivot se bade ya barabar, right mein daalo
    for i in range(len(arr) - 1):  # Last element skip
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    # TODO: Recursively left aur right ko sort karo aur jodo
    return quick_sort(left) + [pivot] + quick_sort(right)


# Test karne ke liye:
print(quick_sort([75, 50, 85, 60, 90, 45]))
print(quick_sort([64, 25, 12, 22, 11]))
print(quick_sort([]))
print(quick_sort([5]))
print(quick_sort([1, 2, 3, 4, 5]))
print(quick_sort([5, 4, 3, 2, 1]))