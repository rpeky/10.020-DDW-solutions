
#condense the max heap process into one function, this function uses the recursive version
def max_heapify(arr, h_size, idx):
    curr_pos = idx
    l_child = 2 * idx + 1
    r_child = 2 * idx + 2

    #check left and right child index validity and if there is need to swap
    if (l_child < h_size) and (arr[curr_pos] < arr[l_child]):
        curr_pos = l_child
    #if above is true, we are comparing left and right to see which is larger
    if (r_child < h_size) and (arr[curr_pos] < arr[r_child]):
        curr_pos = r_child

    #swap if heapify conditions are met i.e. index changes
    if curr_pos != idx:
        arr[idx], arr[curr_pos] = arr[curr_pos], arr[idx]
        #check if below satisfies
        max_heapify(arr, h_size, curr_pos)

def heapsort(arr):
    ar_size = len(arr)

    #convert arr to a maxheap
    for i in range(ar_size//2-1, -1, -1):
        max_heapify(arr, ar_size, i)

    #push the largest value in heap (value in index 0) to the last position in the array continue until the whole array is sorted
    for j in range(ar_size-1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        #make the array a maxheap again, but the array now excludes the largest numbers placed at the end in order
        max_heapify(arr, j, 0)

def main():
    test1 = [1, 2, 8, 7, 14, 9, 3, 10, 4, 16]
    heapsort(test1)
    print(test1)

if __name__ == "__main__":
    main()
