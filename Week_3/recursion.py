
#summation of elements in array done iteratively
def iter_sum(arr):
    sol = 0
    for i in arr:
        sol += i
    return sol

#summation of elements in array done recursively
#use list slicing
#check if there are still elements in the list
def rec_sum(arr):
    #base case - there are no more numbers to add
    if len(arr) == 0:
        return 0
    return arr[0] + rec_sum(arr[1:])
    #return arr[0] + rec_sum(arr[1:]) if arr else 0

#we assume no need for error checking, but n has to be an integer greater than 0
def iter_fac(n):
    sol = 1
    #start from 1 since multiplying with 0 will give 0, shift end by one since it is excluded
    for i in range(1, n+1):
        sol*=i
    return sol

def rec_fac(n):
    #base case, check if n becomes 1 or 0
    if n<=1:
        return 1
    else:
        return n*rec_fac(n-1)

class towers():
    def __init__(self, name):
        self.tower_ID = name
        self.state=list()

    def __del__(self):
        print("State of tower {}: ".format(self.tower_ID), self.state)
        #print("deleting tower {}".format(self.tower_ID))

    #new block must be smaller than the previous block
    def error_check(self, blocksize):
        if len(self.state)!=0:
            return blocksize<self.state[-1]
        else:
            return True

    def operation_add_block(self, block_size):
        if self.error_check(block_size):
            self.state.append(block_size)
        else:
            print("GG error")
            del()

    def operation_remove_block(self):
        return self.state.pop(-1)

#tower of hanoi - say real can cry  
#rules:
#one disc moves at each time
#larger disc cannot be placed on top of smaller disc
def rec_towerofhanoi(n_disc, src, dest, aux):
    #base case do final swap
    if n_disc>=1:
        rec_towerofhanoi(n_disc-1, src, aux, dest)
        dest.operation_add_block(src.operation_remove_block())
        rec_towerofhanoi(n_disc-1, aux, dest, src)

def main():
    #spawn towers
    t_A = towers("A")
    t_B = towers("B")
    t_C = towers("C")
    #add disc into source tower, size must go from largest to smallestfor i in range(3, -1, -1):
    discs = 5
    for i in range(discs, 0, -1):
        t_A.operation_add_block(i)
    rec_towerofhanoi(discs, t_A, t_B, t_C)


if __name__ == "__main__":
    main()
