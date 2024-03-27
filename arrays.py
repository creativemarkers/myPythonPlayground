def reverseArray(array):
    #reverse array in memory O(n)
    #works with even or odd
    l = 0
    r = len(array) - 1

    while l <= r:
        buffer = array[l]
        array[l] = array[r]
        array[r] = buffer
        l += 1
        r -= 1

    return array


def twoPointerLinearSearch(searchArg, array):
    #useless way to linear search, since every element is still being checked
    l = 0
    r = len(array) - 1

    while l <= r:

        if array[l] == searchArg:
            return l
        elif array[r] == searchArg:
            return r
        else:
            l += 1
            r -= 1
    
    return print("Not found")




def main():
    
    array = [1,2,3,4,5,6]
    array = reverseArray(array)
    print(array)
    searchPos = twoPointerLinearSearch(2, array)
    print(searchPos)

if __name__ == "__main__":
    main()