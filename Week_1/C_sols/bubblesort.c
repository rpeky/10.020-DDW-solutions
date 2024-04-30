#include <stdio.h>
#include <stdlib.h>

void bubblesort_optimised(int *arr, int len){
	int swap = 1;
	while(swap==1){
		swap=0;
		for(int i=0;i<len-1;++i){
			if(arr[i]>arr[i+1]){
				int temp = arr[i];
				arr[i]=arr[i+1];
				arr[i+1]=temp;
				swap=1;
			}
		}
		--len;
	}
}

int main(int argc, char **argv){
	int ar[argc-1];
	for(int i=1;i<argc;++i)
		ar[i-1]=strtol(argv[i],NULL,10);
	bubblesort_optimised(ar,argc-1);
	printf("Sorted: \n");
	for(int i=0;i<argc-1;++i)
		printf("%d\n",ar[i]);
	return 0;
}
