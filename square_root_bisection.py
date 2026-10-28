def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # 1. Negative check
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    # 2. 0 aur 1 ke liye special case
    if square_target == 0:
        print("The square root of 0 is 0")
        return 0 
    if square_target == 1:
        print("The square root of 1 is 1")
        return 1

    # 3. Bounds set karo
    low = 0
    # Agar number 1 se chhota hai (jaise 0.25 ya 0.001), toh high 1 hona chahiye.
    if square_target < 1:
        high = 1
    else:
        high = square_target

    # 4. Main Loop
    for i in range(max_iterations):
        mid = (low + high) / 2
        square_mid = mid * mid

        # Tolerance Check: Jab high aur low ka difference bahut chhota ho jaye
        if (high - low) / 2 <= tolerance:
            print(f"The square root of {square_target} is approximately {mid}")
            return mid

        # Binary Search Logic
        if square_mid < square_target:
            low = mid
        else:
            high = mid

    # 5. Agar loop khatam ho gaya aur answer nahi mila
    print(f"Failed to converge within {max_iterations} iterations")
    return None