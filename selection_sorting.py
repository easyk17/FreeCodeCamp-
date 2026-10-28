def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # TODO: Maan lo min_index = i hai
        min_index = i

        # TODO: Ek aur loop chalao j se i+1 se n tak
        # Agar arr[j] chhota hai arr[min_index] se, toh min_index = j kar do

        # TODO: Agar min_index aur i alag hain, toh dono ko swap kar do
        # Hint: Python mein swap karne ke liye: arr[i], arr[min_index] = arr[min_index], arr[i]
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        

    return arr

# Test karne ke liye:
print(selection_sort([64, 25, 12, 22, 11]))
# Test cases
print(selection_sort([64, 25, 12, 22, 11]))   # Normal
print(selection_sort([]))                     # Empty array
print(selection_sort([5]))                    # Single element
print(selection_sort([1, 2, 3, 4, 5]))        # Already sorted
print(selection_sort([5, 4, 3, 2, 1]))        # Reverse sorted
print(selection_sort([3, 3, 2, 1, 1]))        # Duplicates
print(selection_sort([-5, 0, 10, -2, 7]))     # Negative numbers