#divide and conquer

#merge sort invovles splitting the array in half until there is only one element left 
#then proceed to build back up the array upwards by comparing the adjacent array
#repeat until we get back the array but sorted

def merge(ls_1, ls_2):
    merged = list()
    #check if list are in range
    i,j = 0,0
    while(i<len(ls_1) and j<len(ls_2)):
        #assign from smallest to largest to merged result
        if ls_1[i]<ls_2[j]:
            merged.append(ls_1[i])
            i+=1
        else:
            merged.append(ls_2[j])
            j+=1
    #leftover case if the two input array are different length
    while(i<len(ls_1)):
        merged.append(ls_1[i])
        i+=1
    while(j<len(ls_2)):
        merged.append(ls_2[j])
        j+=1
    return merged

def mergesort(unsorted_ls):
    #edgecase length of 1
    if len(unsorted_ls)<2:
        return unsorted_ls
    #set middle index
    n = len(unsorted_ls)//2
    l_arr = mergesort(unsorted_ls[:n])
    r_arr = mergesort(unsorted_ls[n:])

    return merge(l_arr,r_arr)

#more important is the time complexity!
#check the ddw lesson for the calculation but the complexity should be O(nlogn)
def main():
    test1 = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1]
    print("initial : ",test1)
    test2 = mergesort(test1)
    print("sorted : ",test2)

if __name__ == "__main__":
    main()
