#include"stdio.h"
int main(int argc, char* argv[])
{
	int num[100] = { 0 };
	int count = 0;
	for (int i = 1; i < 5; i++) {
		for (int j = 1; j < 5; j++){
			for (int k = 1; k < 5;k++)
				if (i != j &&i != k &&j != k) {
					num[count++] = 100 * i + 10 * j + k;
					printf("%d %d %d\n", i,j,k);
			}
		}		
	}
	printf("number is:%d\n",count);
	for (int i = 0; i < count; i++)
	{
		printf("index %d is:%d\n", i, num[i]);
	}
	return 0;
}