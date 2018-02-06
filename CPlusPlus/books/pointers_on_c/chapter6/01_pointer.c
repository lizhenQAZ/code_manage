#include "stdio.h"

int main(int argc, char const *argv[])
{
	int a=102;
	float c=10.4;
	int* b=&a;
	float* d=&c;
	printf("a=%d,&a=%d,b=%d,*b=%d\n",a,&a,b,*b);
	printf("c=%f,&c=%d,d=%d,*d=%f\n",c,&c,d,*d);
	return 0;
}