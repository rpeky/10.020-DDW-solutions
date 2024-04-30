#300424_peky
#not bubble sort

def insert_v1(ls_unsorted):
    #fixed outer
    #since the comparison checks the previous values, we dont need the first value
    n = len(ls_unsorted)
    #lets count the number of times needed to swap -> number of operations taken
    count1_comparision=0
    count1_swaps=0
    #iterate from index 1 to last index, since n itself is excluded, total iterations looks like 1,2,3...n-2, n-1 where n-1 is the position of the last index
    for idx_outer in range(1,n):
        idx_inner = idx_outer
        #check if there is anything to the left andf is larger than the current, if so swap them
        #in effect,smallest number gets pushed to the left most position of the array/list
        while (idx_inner > 0) and (ls_unsorted[idx_inner-1] > ls_unsorted[idx_inner]):
            ls_unsorted[idx_inner],ls_unsorted[idx_inner-1] = ls_unsorted[idx_inner-1],ls_unsorted[idx_inner]
            idx_inner-=1
            count1_comparision+=1
            #we count 2 swaps since we are exchanging two sets of numbers
            count1_swaps+=2
    return ls_unsorted, count1_comparision, count1_swaps

def insert_v2(ls_unsorted):
    #this time, the improvement is to not swap until the number your are checking is in the right position
    n = len(ls_unsorted)
    count2_comparisons=0
    count2_swaps=0

    for idx_outer in range(1,n):
        idx_inner = idx_outer
        #store the number in the current index (we keep moving right in the outer loop, this number changes every iteration)
        temp_checkval = ls_unsorted[idx_inner]
        #go left until the number on the left is smaller than the value we are checking
        #since we are going from left to right, the left side of the list/array ios always sorted~
        while (idx_inner > 0) and (ls_unsorted[idx_inner - 1] > temp_checkval):
            #shift values to the right to make space
            ls_unsorted[idx_inner] = ls_unsorted[idx_inner-1]
            idx_inner-=1
            count2_comparisons+=1
            #main difference between v1 and v2 is that v2 only swaps once during the comparison
            count2_swaps+=1

            #at the end of this search is the position of the value we are checking
        ls_unsorted[idx_inner] = temp_checkval
        count2_swaps+=1
    return ls_unsorted, count2_comparisons, count2_swaps

def main():
    sample_scrambled_numbers1 = [22, 14, 65, 32, 123, 5534, 321, 0, 1, 2, 55, 139, 8456, 43, 34, 112, 943]
    sample_scrambled_numbers2 = [22, 14, 65, 32, 123, 5534, 321, 0, 1, 2, 55, 139, 8456, 43, 34, 112, 943]

    sol1,comp1,swap1 = insert_v1(sample_scrambled_numbers1)
    sol2,comp2,swap2 = insert_v2(sample_scrambled_numbers2)

    print(sol1, "\nComparisons: {}\nSwaps: {}".format(comp1,swap1))
    print(sol2, "\nComparisons: {}\nSwaps: {}".format(comp2,swap2))

if __name__ == "__main__":
    main()
