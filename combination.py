def subsum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("We found sum(%s)=%s" % (partial, target))
        return True
    if s >= target:
        # if we reach the number why bother to continue
        return False

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        return subsum(remaining, target, partial + [n]) or subsum(remaining, target, partial)

if __name__ == "__main__":
    print("--------------------------------------------------------------------------------------------------------")
    print("Test case 1: [22, 1, 4, 3, 17, 9, 8, 3, 5, 7, 10, 2] and target 207")
    if (not subsum([22, 1, 4, 3, 17, 9, 8, 3, 5, 7, 10, 2], 207) ):
        print("We cannot find any combinations of the integers in the array add up to exactly the given target.")
    print("--------------------------------------------------------------------------------------------------------")    
    print("Test case 2: [22, 1, 4, 3, 17, 9, 8, 3, 5, 7, 10, 2] and target 27")
    if (not subsum([22, 1, 4, 3, 17, 9, 8, 3, 5, 7, 10, 2], 27) ):
        print("We cannot find any combinations of the integers in the array add up to exactly the given target.")
    print("--------------------------------------------------------------------------------------------------------")

