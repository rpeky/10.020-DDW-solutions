#300422_peky
#to illustrate the difference in operations, we will count the number of steps taken with a count variable

def b_sort_v1(ls_unsorted):
    #since the operations for swapping are the same throughout, we are counting the number of iterations needed to achieve the sort
    count = 0
    #iterate through unsorted list
    #to access next number, we want the index of the position to check
    #hence we need an index variable idx
    #range(len(ls_unsorted)) generates the range to iterate from 0 , 1, 2 ... length of list - 1 (check CTD notes or pyhton documentation if not sure of reason)
    for idx_outer in range(len(ls_unsorted)-1):
        #two for loops since we need to iterate for every number in the list, then for each number sort them into its place
        #bubble sort always pushes the largest number to the end of the list, and we need to do this for each number
        #hence two for loops are needed

        #for this example we'll sort on the spot using the given list/array, copy the list if you want to preserve the initial list

        #compare the current number and the next number
        #correct order is smaller , larger
        #can be compared using comparison operator < or > see your preference
        #if is correct, do nothin -> means only one if statement is needed
        #access number using nameoflist/array [ index ]
        for idx_inner in range(len(ls_unsorted)-1):
            count+=1
            if(ls_unsorted[idx_inner] > ls_unsorted[idx_inner + 1]):
                temp = ls_unsorted[idx_inner]
                ls_unsorted[idx_inner] = ls_unsorted[idx_inner + 1]
                ls_unsorted[idx_inner + 1] = temp

                #alternatively ls_unsorted[idx], ls_unsorted[idx+1] = ls_unsorted[idx+1], ls_unsorted[idx]

    return ls_unsorted, count


def b_sort_v2(ls_unsorted):
    #for v2 we realise that if there were no swaps made in the loop, that means that the numbers are already in order and we can stop early
    count2 = 0
    swaps = True
    while swaps:
        swaps = False
        for idx_inner in range(len(ls_unsorted)-1):
            count2+=1
            if(ls_unsorted[idx_inner] > ls_unsorted[idx_inner + 1]):
                temp = ls_unsorted[idx_inner]
                ls_unsorted[idx_inner] = ls_unsorted[idx_inner + 1]
                ls_unsorted[idx_inner + 1] = temp
                #alternatively ls_unsorted[idx], ls_unsorted[idx+1] = ls_unsorted[idx+1], ls_unsorted[idx]

                swaps = True


    return ls_unsorted, count2

def b_sort_v3(ls_unsorted):
    #for v3 we realise that the last value is always correct after each iteration, so we can choose not to check the sorted values
    #this is achieved by reducing the range to iterate through by the number of iterations
    count3 = 0
    swaps = True
    list_len = len(ls_unsorted)-1
    while swaps:
        swaps = False
        for idx_inner in range(list_len):
            count3 +=1
            if(ls_unsorted[idx_inner] > ls_unsorted[idx_inner + 1]):
                temp = ls_unsorted[idx_inner]
                ls_unsorted[idx_inner] = ls_unsorted[idx_inner + 1]
                ls_unsorted[idx_inner + 1] = temp
                #alternatively ls_unsorted[idx], ls_unsorted[idx+1] = ls_unsorted[idx+1], ls_unsorted[idx]

                swaps = True

        #reduce the number of searches after each sort since the last values to this point are correct
        list_len-=1

    return ls_unsorted, count3

def b_sort_v4(ls_unsorted):
    #for v4 we realise that that we can reduce the sort even further by shifting the last element to sort even further
    #we only need to search until the position of the last swap, since the bigger number is in the correct place, the end point should be the index of the smaller number
    count4 = 0
    swaps = True
    list_len = len(ls_unsorted)-1
    while swaps:
        swaps = False
        new_list_len = 0
        for idx_inner in range(list_len):
            count4+=1
            if(ls_unsorted[idx_inner] > ls_unsorted[idx_inner + 1]):
                temp = ls_unsorted[idx_inner]
                ls_unsorted[idx_inner] = ls_unsorted[idx_inner + 1]
                ls_unsorted[idx_inner + 1] = temp
                #alternatively ls_unsorted[idx], ls_unsorted[idx+1] = ls_unsorted[idx+1], ls_unsorted[idx]

                #if swapped we set the position of the new range ot the index of the smaller number
                new_list_len = idx_inner
                swaps = True
        #set new range to search until
        list_len=new_list_len

    return ls_unsorted, count4



def main():
    sample_scrambled_numbers1 = [82, 65, 93, 0, 60, 31, 99, 90, 31, 70, 1, 2, 12, 32, 15, 105, 107, 108]
    sample_scrambled_numbers2 = [82, 65, 93, 0, 60, 31, 99, 90, 31, 70, 1, 2, 12, 32, 15, 105, 107, 108]
    sample_scrambled_numbers3 = [82, 65, 93, 0, 60, 31, 99, 90, 31, 70, 1, 2, 12, 32, 15, 105, 107, 108]
    sample_scrambled_numbers4 = [82, 65, 93, 0, 60, 31, 99, 90, 31, 70, 1, 2, 12, 32, 15, 105, 107, 108]
    
    solv1,stepsv1 = b_sort_v1(sample_scrambled_numbers1)
    print(solv1, "\nSteps taken to sort: {}".format(stepsv1))
    solv2,stepsv2 = b_sort_v2(sample_scrambled_numbers2)
    print(solv2, "\nSteps taken to sort: {}".format(stepsv2))
    solv3,stepsv3 = b_sort_v3(sample_scrambled_numbers3)
    print(solv3, "\nSteps taken to sort: {}".format(stepsv3))
    solv4,stepsv4 = b_sort_v4(sample_scrambled_numbers4)
    print(solv4, "\nSteps taken to sort: {}".format(stepsv4))


if __name__ == "__main__":
    main()
