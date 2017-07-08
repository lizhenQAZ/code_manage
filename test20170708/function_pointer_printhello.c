#include "stdio.h"
void sayhello()
{
	printf("hello c!\n");
}

int main(int argc, char const *argv[])
{
	void (*p)();
	p=sayhello;
	p();
	return 0;
}