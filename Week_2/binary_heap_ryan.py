#300424_peky

#how to calculate the index of the parent node
#find index of current node
#since the tree always splits into 2 downwards, the daughter node index is always parent node * 2 +1 | +2
#this *2 is to account for the opposite parent on the other side of the tree and the daughter nodes from one level up
#try drawing it 

def daughter_index(parent_index):
    d1 = parent_index + 1
    d2 = parent_index + 2
    return d1, d2

#the parent index is the opposite, for the odd index, subtract 1 and divide by 2
#for the even index, we take advantage of the truncation done by typecasting int over the float
#this makes it that we can always subtract by 1 and divide by 2 to find the parent instead of checking for even odd

def parent_index(daughter_index):
    return int((daughter_index-1)/2)

#specifically find left daughter
#apply above
def left_orphan(parent_idx):
    return (parent_idx * 2) + 1

def right_orphan(parent_idx):
    return (parent_idx * 2) + 2


#max-heap
#we want to check if the order of numbers are correct, the higher the index, the higher the value
#every node has at most two children

#full binary tree conditions
#all nodes (other than root) has a parent
#all nodes have two children other than leaves (last node in the tree)
#i.e. all nodes have either 0 or 2 child nodes

#complete binary tree conditons
#all nodes have maximum child nodes other than last level
#leaves must fill from the left


def heapify_max_v1(arr, index):
    curr_pos = index
    while((left_orphan(curr_pos) < len(arr)) and swapped):
        #check if children nodes are in range
        L_child = left_orphan(curr_pos)
        R_child = right_orphan(curr_pos)
        #find the index of larger child node to check if it is larger than current node value
        #use ternary to check if left is larger else right, or do an if else statement
        if(R_child < len(arr)):
           fat_child = L_child if (arr[L_child] > arr[R_child]) else R_child
        else:
           fat_child = L_child
        #check if child is larger, if so swap
        if arr[fat_child] > arr[curr_pos]:
            arr[fat_child], arr[curr_pos] = arr[curr_pos], arr[fat_child]
        curr_pos = fat_child

#we can improve the algo by stopping early
#if there is no swaps, this implies that the child nodes already satisfy the max heapify condition
def heapify_max_v2(arr, index):
    curr_pos = index
    swapped = True
    #check if child is the last node
    while((left_orphan(curr_pos) < len(arr)) and swapped):
        #set swapped as false, if no swaps happen means that tree is max heapified and no more checks are needed
        swapped = False
        #check if children nodes are in range
        L_child = left_orphan(curr_pos)
        R_child = right_orphan(curr_pos)
        #find the index of larger child node to check if it is larger than current node value
        #use ternary to check if left is larger else right, or do an if else statement
        if R_child < len(arr):
            fat_child = L_child if (arr[L_child] > arr[R_child]) else R_child
        else:
            fat_child = L_child
        #check if child is larger, if so swap
        if arr[fat_child] > arr[curr_pos]:
            arr[fat_child], arr[curr_pos] = arr[curr_pos], arr[fat_child]
            swapped = True
        curr_pos = fat_child

def build_max_heap(arr):
    #set the start point as the middle value, since in a binary tree, the middle value will be one away from the leaf
    #this allows us to travel the tree
    len_arr = len(arr)
    start_index = int(len_arr/2)-1
    #iterate through the tree upwards, max_heapify will check downwards for us, hence we can check the whole tree from this point 
    for i in range(start_index,-1,-1):
        heapify_max_v2(arr, i)

def main():
    test_tree = [1, 2, 8, 7, 14, 9, 3, 10, 4, 16]
    build_max_heap(test_tree)
    for i in range(len(test_tree)):
        print("Index {}".format(i))
        print("Value {}".format(test_tree[i]))
    print(test_tree)

if __name__ == "__main__":
    main()
